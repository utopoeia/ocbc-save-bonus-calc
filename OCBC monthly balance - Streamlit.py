import streamlit as st
import datetime as dt
import calendar

st.set_page_config(page_title="OCBC Save Bonus Calculator", page_icon="💰")

st.title("💰 OCBC Save Bonus Calculator")

st.markdown("""
This tool helps you calculate how much balance you need to maintain in your OCBC 365/360 account 
to qualify for the Save Bonus (i.e. $500 increase in average daily balance).
""")

# Input fields
monthly_balance = st.number_input("Current monthly balance ($)", min_value=0.0, format="%.2f")
monthly_balance_change = st.number_input("Monthly balance change vs last month ($)", format="%.2f")
ledger_bal = st.number_input("Current ledger balance ($)", min_value=0.0, format="%.2f")

if st.button("Calculate"):
    try:
        # Calculation
        target_monthly_balance = monthly_balance - monthly_balance_change + 500
        now = dt.datetime.now()
        num_days_in_month = calendar.monthrange(now.year, now.month)[1]
        days_passed = now.day - 1
        days_left_in_month = num_days_in_month - days_passed

        if days_left_in_month <= 0:
            st.error("No days left in the month! Try again next month.")
        else:
            acct_bal_to_maintain = (
                                               target_monthly_balance * num_days_in_month - days_passed * monthly_balance) / days_left_in_month
            amount_to_withdraw = ledger_bal - acct_bal_to_maintain

            st.success(f"✅ Number of days left in the month: **{days_left_in_month}**")
            st.success(f"✅ Target monthly balance: **${target_monthly_balance:,.2f}**")
            st.success(f"✅ You need to withdraw: **${amount_to_withdraw:,.2f}**")

    except Exception as e:
        st.error(f"Error in calculation: {e}")