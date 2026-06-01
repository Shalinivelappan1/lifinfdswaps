import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import random
from datetime import datetime

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Experiential Swaps Lab",
    page_icon="🔄",
    layout="wide"
)

# =========================================================
# HELPER FUNCTIONS
# =========================================================

def currency(x):
    return f"₹{x:,.2f}"

def pct(x, d=2):
    return f"{round(x, d)}%"

def bps(x):
    return f"{round(x,2)} bps"

# =========================================================
# TITLE
# =========================================================

st.title("🔄 Experiential Learning Lab — Swaps")

st.markdown("""
Welcome to the **Swaps Learning Platform**.

This lab covers:

- Interest Rate Swaps
- Currency Swaps
- Commodity Swaps
- Equity Swaps
- OIS Swaps
- Comparative Advantage
- Cash Flow Simulation
- Treasury Analytics
""")

# =========================================================
# SIDEBAR
# =========================================================

menu = st.sidebar.radio("Choose Module", [

    # Basics
    "Introduction to Swaps",
    "Interest Rate Swaps",
    "Currency Swaps",
    "Commodity Swaps",
    "Equity Swaps",
    "Comparative Advantage",
    "Swap Cash Flow Simulator",

    # Valuation
    "Swap Pricing & Valuation",
    "Advanced Swap Valuation",
    "Swap Curve & Yield Curve",
    "Yield Curve Bootstrapping",
    "Mark-to-Market",
    "DV01 & Duration Analysis",
    "Interest Rate Sensitivity",
    "Stress Testing",
    "Scenario Analysis",

    # Risk
    "Counterparty Risk",
    "Exposure Profile",
    "Collateral Simulation",
    "CSA Logic",
    "Central Clearing",
    "CVA Basics",
    "Advanced CVA",
    "XVA Overview",

     # CDS
    "Credit Default Swaps",
    "CDS Spread Calculator",
    "CDS Payoff Simulator",
    "CDS vs Bond Spread",
    "Credit Event Simulator",
    "Sovereign CDS Monitor",

    # Treasury
    "Treasury Desk Simulator",
    "Treasury Roleplay",
    "Hedge Recommendation Engine",
    "Multi-Risk Treasury Dashboard",
    "ALM Simulator",
    "Treasury War Room",
    "Live Strategy Engine",

    # Indian Market
    "MIFOR Swaps",
    "Indian Swaps Market",
    "OIS Swaps",
    "Benchmark Transition",

    # Learning
    "Swap Timeline Visualizer",
    "Swaps vs Futures vs Forwards",
    "Case-Based Learning",
    "Step-by-Step Solver",
    "Quiz Engine",
    "Formula Cheat Sheet",
    "Common Student Mistakes",

    # Advanced
    "Swaptions",
    "Swaption Payoff Visualizer",
    "Monte Carlo Rate Simulation",
    "Portfolio Swap Analytics",
    "Hedge Effectiveness",
    "Hedge Accounting",

    # Institutional
    "Gamified Learning",
    "Faculty Mode",
    "Executive Education Mode",
    "Treasury Scorecard",
    "Capstone Simulation",
    "Learning Progress Tracker",
    "Badge System",
    "Interactive Timeline Engine",
    "Swap Dashboard",
    "Swap Market Simulator",

    # Output
    "Report Generator",
    "Certificate Generator",
    "Finance UI Enhancements"

])

# =========================================================
# INTRODUCTION
# =========================================================

if menu == "Introduction to Swaps":

    st.header("📘 Introduction to Swaps")

    st.markdown("""
## What is a Swap?

A swap is an OTC derivative contract where two parties exchange
cash flows over time.

---

## Major Types

| Swap Type | Exchange |
|---|---|
| Interest Rate Swap | Fixed ↔ Floating |
| Currency Swap | Currency Cash Flows |
| Commodity Swap | Fixed ↔ Commodity Price |
| Equity Swap | Equity Return ↔ Interest |

---

## Applications

### Hedging
- Interest-rate risk
- Currency exposure
- Commodity price volatility

### Treasury Management
- Asset-liability matching
- Cost reduction

### Speculation
- Rate expectations
- Currency views
""")

# =========================================================
# INTEREST RATE SWAPS
# =========================================================

elif menu == "Interest Rate Swaps":

    st.header("📈 Interest Rate Swaps")

    st.markdown("""
## Plain Vanilla IRS

One party:
- pays fixed
- receives floating

Other party:
- pays floating
- receives fixed
""")

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Notional Principal",
            value=10000000.0
        )

        fixed_rate = st.number_input(
            "Fixed Rate (%)",
            value=7.0
        )

    with col2:

        floating_rate = st.number_input(
            "Floating Rate (%)",
            value=6.5
        )

        years = st.number_input(
            "Tenure (Years)",
            value=5
        )

    fixed_payment = principal * fixed_rate/100
    floating_payment = principal * floating_rate/100

    net_payment = floating_payment - fixed_payment

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Fixed Leg",
        currency(fixed_payment)
    )

    col2.metric(
        "Floating Leg",
        currency(floating_payment)
    )

    col3.metric(
        "Net Settlement",
        currency(net_payment)
    )

# =========================================================
# CURRENCY SWAPS
# =========================================================

elif menu == "Currency Swaps":

    st.header("💱 Currency Swaps")

    st.markdown("""
A currency swap exchanges:
- principal
- interest payments
- principal at maturity
""")

    col1, col2 = st.columns(2)

    with col1:

        inr_principal = st.number_input(
            "INR Principal",
            value=100000000.0
        )

        usd_principal = st.number_input(
            "USD Principal",
            value=1200000.0
        )

    with col2:

        inr_rate = st.number_input(
            "INR Rate (%)",
            value=7.5
        )

        usd_rate = st.number_input(
            "USD Rate (%)",
            value=5.0
        )

    inr_interest = inr_principal * inr_rate/100
    usd_interest = usd_principal * usd_rate/100

    col1, col2 = st.columns(2)

    col1.metric(
        "Annual INR Interest",
        currency(inr_interest)
    )

    col2.metric(
        "Annual USD Interest",
        f"${usd_interest:,.2f}"
    )

# =========================================================
# COMMODITY SWAPS
# =========================================================

elif menu == "Commodity Swaps":

    st.header("🛢️ Commodity Swaps")

    fixed_price = st.number_input(
        "Fixed Commodity Price",
        value=6500.0
    )

    market_price = st.number_input(
        "Market Price",
        value=7200.0
    )

    quantity = st.number_input(
        "Quantity",
        value=1000.0
    )

    payoff = (
        market_price - fixed_price
    ) * quantity

    st.metric(
        "Commodity Swap Payoff",
        currency(payoff)
    )

# =========================================================
# EQUITY SWAPS
# =========================================================

elif menu == "Equity Swaps":

    st.header("📊 Equity Swaps")

    notional = st.number_input(
        "Notional Amount",
        value=10000000.0
    )

    equity_return = st.number_input(
        "Equity Return (%)",
        value=12.0
    )

    fixed_rate = st.number_input(
        "Fixed Rate (%)",
        value=7.0
    )

    equity_leg = notional * equity_return/100
    fixed_leg = notional * fixed_rate/100

    net = equity_leg - fixed_leg

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Equity Leg",
        currency(equity_leg)
    )

    col2.metric(
        "Fixed Leg",
        currency(fixed_leg)
    )

    col3.metric(
        "Net Swap Value",
        currency(net)
    )

# =========================================================
# COMPARATIVE ADVANTAGE
# =========================================================

elif menu == "Comparative Advantage":

    st.header("⚖️ Comparative Advantage Theory")

    st.markdown("""
Swaps often arise because firms have different borrowing advantages.
""")

    col1, col2 = st.columns(2)

    with col1:

        a_fixed = st.number_input(
            "Company A Fixed Rate (%)",
            value=7.0
        )

        a_float = st.number_input(
            "Company A Floating Rate (%)",
            value=6.0
        )

    with col2:

        b_fixed = st.number_input(
            "Company B Fixed Rate (%)",
            value=9.0
        )

        b_float = st.number_input(
            "Company B Floating Rate (%)",
            value=7.5
        )

    fixed_advantage = b_fixed - a_fixed
    float_advantage = b_float - a_float

    total_gain = fixed_advantage - float_advantage

    st.metric(
        "Total Gain from Swap",
        pct(total_gain)
    )

# =========================================================
# CASH FLOW SIMULATOR
# =========================================================

elif menu == "Swap Cash Flow Simulator":

    st.header("💸 Swap Cash Flow Simulator")

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Notional Principal",
            value=10000000.0,
            key="cf_principal"
        )

        fixed_rate = st.number_input(
            "Fixed Rate (%)",
            value=7.0,
            key="cf_fixed"
        )

        periods = st.slider(
            "Number of Periods",
            1,
            20,
            10
        )

    with col2:

        floating_mean = st.number_input(
            "Average Floating Rate (%)",
            value=6.5
        )

        floating_vol = st.number_input(
            "Floating Rate Volatility",
            value=0.8
        )

    floating_rates = np.random.normal(
        floating_mean,
        floating_vol,
        periods
    )

    fixed_cf = [
        principal * fixed_rate/100
        for _ in range(periods)
    ]

    floating_cf = [
        principal * r/100
        for r in floating_rates
    ]

    net_cf = np.array(floating_cf) - np.array(fixed_cf)

    df = pd.DataFrame({

        "Period": np.arange(1, periods+1),
        "Floating Rate": floating_rates,
        "Fixed Cash Flow": fixed_cf,
        "Floating Cash Flow": floating_cf,
        "Net Settlement": net_cf

    })

    st.dataframe(df, use_container_width=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Period"],
        y=df["Net Settlement"],
        mode='lines+markers',
        name='Net Settlement'
    ))

    fig.update_layout(
        title="Swap Net Cash Flows Through Time",
        xaxis_title="Period",
        yaxis_title="Cash Flow"
    )

    st.plotly_chart(fig, use_container_width=True)
# =========================================================
# SWAP PRICING & VALUATION
# =========================================================

elif menu == "Swap Pricing & Valuation":

    st.header("💰 Swap Pricing & Valuation")

    st.markdown("""
## Swap Valuation

Swap Value:

Swap Value = PV(Floating Leg) − PV(Fixed Leg)

At initiation:
- swap value ≈ zero

As rates move:
- swap gains/losses emerge.
""")

    col1, col2 = st.columns(2)

    with col1:

        pv_fixed = st.number_input(
            "PV of Fixed Leg",
            value=9800000.0
        )

    with col2:

        pv_floating = st.number_input(
            "PV of Floating Leg",
            value=10100000.0
        )

    swap_value = pv_floating - pv_fixed

    st.metric(
        "Swap Market Value",
        currency(swap_value)
    )

    if swap_value > 0:

        st.success("""
Swap has positive value to floating-rate receiver.
""")

    else:

        st.warning("""
Swap has negative value.
""")

# =========================================================
# ADVANCED SWAP VALUATION
# =========================================================

elif menu == "Advanced Swap Valuation":

    st.header("🏦 Advanced Swap Valuation")

    st.markdown("""
This module values:
- fixed leg
- floating leg
- total swap value

using:
- discount factors
- present values
- future floating-rate projections
""")

    col1, col2 = st.columns(2)

    with col1:

        principal = st.number_input(
            "Principal",
            value=10000000.0
        )

        fixed_coupon = st.number_input(
            "Fixed Coupon (%)",
            value=7.0
        )

        maturity = st.number_input(
            "Maturity (Years)",
            value=5
        )

    with col2:

        discount_rate = st.number_input(
            "Discount Rate (%)",
            value=6.5
        )

        payments = st.selectbox(
            "Payments Per Year",
            [1, 2, 4]
        )

    dt = 1/payments

    n_periods = maturity * payments

    periods = np.arange(1, n_periods+1)

    discount_factors = [

        1 / ((1 + discount_rate/100/payments)**t)

        for t in periods

    ]

    fixed_cashflows = [

        principal * fixed_coupon/100 * dt

        for _ in periods

    ]

    fixed_cashflows[-1] += principal

    floating_rates = np.random.normal(
        6.5,
        0.75,
        n_periods
    )

    floating_cashflows = [

        principal * r/100 * dt

        for r in floating_rates

    ]

    floating_cashflows[-1] += principal

    pv_fixed = np.sum(
        np.array(fixed_cashflows) * np.array(discount_factors)
    )

    pv_float = np.sum(
        np.array(floating_cashflows) * np.array(discount_factors)
    )

    swap_value = pv_float - pv_fixed

    valuation_df = pd.DataFrame({

        "Period": periods,
        "Discount Factor": discount_factors,
        "Floating Rate": floating_rates,
        "Fixed CF": fixed_cashflows,
        "Floating CF": floating_cashflows

    })

    st.dataframe(
        valuation_df,
        use_container_width=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "PV Fixed Leg",
        currency(pv_fixed)
    )

    col2.metric(
        "PV Floating Leg",
        currency(pv_float)
    )

    col3.metric(
        "Swap Value",
        currency(swap_value)
    )

# =========================================================
# SWAP CURVE & YIELD CURVE
# =========================================================

elif menu == "Swap Curve & Yield Curve":

    st.header("📈 Swap Curve & Yield Curve")

    st.markdown("""
## Yield Curve

A yield curve shows:
- interest rates
- across maturities

Used for:
- swap pricing
- discounting
- treasury valuation
- risk management
""")

    maturities = [1, 2, 3, 5, 7, 10]

    st.subheader("Input Swap Rates")

    cols = st.columns(len(maturities))

    rates = []

    for i, m in enumerate(maturities):

        with cols[i]:

            r = st.number_input(
                f"{m}Y (%)",
                value=float(6 + i*0.2),
                key=f"curve_{i}"
            )

            rates.append(r)

    curve_df = pd.DataFrame({

        "Maturity": maturities,
        "Swap Rate": rates

    })

    st.dataframe(curve_df, use_container_width=True)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=maturities,
        y=rates,
        mode='lines+markers',
        name='Swap Curve'
    ))

    fig.update_layout(
        title="Swap Yield Curve",
        xaxis_title="Maturity (Years)",
        yaxis_title="Interest Rate (%)"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# YIELD CURVE BOOTSTRAPPING
# =========================================================

elif menu == "Yield Curve Bootstrapping":

    st.header("📊 Yield Curve Bootstrapping")

    st.markdown("""
Bootstrapping derives:
- spot rates
- discount factors
- zero-coupon curve
""")

    maturities = [1, 2, 3, 5, 7, 10]

    cols = st.columns(len(maturities))

    spot_rates = []

    for i, m in enumerate(maturities):

        with cols[i]:

            r = st.number_input(
                f"{m}Y Spot (%)",
                value=float(6 + i*0.25),
                key=f"boot_{i}"
            )

            spot_rates.append(r)

    discount_factors = [

        1 / ((1 + r/100)**m)

        for r, m in zip(
            spot_rates,
            maturities
        )

    ]

    boot_df = pd.DataFrame({

        "Maturity": maturities,
        "Spot Rate": spot_rates,
        "Discount Factor": discount_factors

    })

    st.dataframe(
        boot_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=maturities,
        y=discount_factors,
        mode='lines+markers',
        name='Discount Factors'
    ))

    fig.update_layout(
        title="Discount Factor Curve",
        xaxis_title="Maturity",
        yaxis_title="Discount Factor"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# MARK TO MARKET
# =========================================================

elif menu == "Mark-to-Market":

    st.header("📊 Swap Mark-to-Market")

    st.markdown("""
Swap values change continuously because:
- interest rates move
- yield curves shift
- discount factors change
""")

    months = st.slider(
        "Number of Months",
        6,
        36,
        12
    )

    volatility = st.number_input(
        "MTM Volatility",
        value=300000.0
    )

    mtm = np.random.normal(
        0,
        volatility,
        months
    ).cumsum()

    mtm_df = pd.DataFrame({

        "Month": np.arange(1, months+1),
        "MTM Value": mtm

    })

    st.dataframe(
        mtm_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=mtm_df["Month"],
        y=mtm_df["MTM Value"],
        mode='lines+markers',
        name='MTM'
    ))

    fig.update_layout(
        title="Swap MTM Evolution",
        xaxis_title="Month",
        yaxis_title="Market Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# DV01 & DURATION ANALYSIS
# =========================================================

elif menu == "DV01 & Duration Analysis":

    st.header("📉 DV01 & Duration Analysis")

    st.markdown("""
DV01 measures:
- dollar value change
- for a 1 basis point movement in rates
""")

    col1, col2 = st.columns(2)

    with col1:

        market_value = st.number_input(
            "Swap Market Value",
            value=10000000.0
        )

        duration = st.number_input(
            "Swap Duration",
            value=4.5
        )

    with col2:

        bp_change = st.slider(
            "Rate Change (bps)",
            -200,
            200,
            25
        )

    dv01 = market_value * duration * 0.0001

    estimated_change = -dv01 * bp_change

    col1, col2 = st.columns(2)

    col1.metric(
        "DV01",
        currency(dv01)
    )

    col2.metric(
        "Estimated MTM Change",
        currency(estimated_change)
    )

# =========================================================
# INTEREST RATE SENSITIVITY
# =========================================================

elif menu == "Interest Rate Sensitivity":

    st.header("📈 Interest Rate Sensitivity")

    base_value = st.number_input(
        "Current Swap Value",
        value=10000000.0
    )

    duration = st.number_input(
        "Duration",
        value=4.0
    )

    shocks = np.arange(
        -200,
        225,
        25
    )

    value_changes = [

        -base_value * duration * s/10000

        for s in shocks

    ]

    sens_df = pd.DataFrame({

        "Rate Shock (bps)": shocks,
        "Value Change": value_changes

    })

    st.dataframe(
        sens_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=sens_df["Rate Shock (bps)"],
        y=sens_df["Value Change"],
        mode='lines+markers'
    ))

    fig.update_layout(
        title="Swap Sensitivity to Interest Rates",
        xaxis_title="Rate Shock (bps)",
        yaxis_title="Value Change"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# STRESS TESTING
# =========================================================

elif menu == "Stress Testing":

    st.header("⚠️ Stress Testing")

    portfolio_value = st.number_input(
        "Portfolio Value",
        value=50000000.0
    )

    duration = st.number_input(
        "Portfolio Duration",
        value=5.0
    )

    stress_scenarios = {

        "Mild Stress (+50bps)": 50,
        "Moderate Stress (+100bps)": 100,
        "Severe Stress (+200bps)": 200,
        "Extreme Stress (+400bps)": 400

    }

    results = []

    for scenario, shock in stress_scenarios.items():

        pnl = -portfolio_value * duration * shock/10000

        results.append({

            "Scenario": scenario,
            "Shock (bps)": shock,
            "Estimated P&L": pnl

        })

    stress_df = pd.DataFrame(results)

    st.dataframe(
        stress_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=stress_df["Scenario"],
        y=stress_df["Estimated P&L"]
    ))

    fig.update_layout(
        title="Stress Test Results",
        xaxis_title="Scenario",
        yaxis_title="Portfolio P&L"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# SCENARIO ANALYSIS
# =========================================================

elif menu == "Scenario Analysis":

    st.header("🎯 Scenario Analysis")

    current_swap_value = st.number_input(
        "Current Swap Value",
        value=10000000.0
    )

    duration = st.number_input(
        "Duration",
        value=4.5
    )

    scenario_rates = [

        -150,
        -100,
        -50,
        0,
        50,
        100,
        150

    ]

    scenario_values = []

    for shock in scenario_rates:

        value = current_swap_value - (
            current_swap_value * duration * shock/10000
        )

        scenario_values.append(value)

    scenario_df = pd.DataFrame({

        "Rate Shock (bps)": scenario_rates,
        "Swap Value": scenario_values

    })

    st.dataframe(
        scenario_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=scenario_df["Rate Shock (bps)"],
        y=scenario_df["Swap Value"],
        mode='lines+markers'
    ))

    fig.update_layout(
        title="Scenario Analysis of Swap Value",
        xaxis_title="Interest Rate Shock",
        yaxis_title="Swap Value"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )
# =========================================================
# COUNTERPARTY RISK
# =========================================================

elif menu == "Counterparty Risk":

    st.header("⚠️ Counterparty Risk")

    st.markdown("""
## Counterparty Risk

Swaps are OTC contracts.

Risk:
One counterparty may default before maturity.

---

## Sources of Risk

- MTM exposure
- Interest-rate volatility
- Credit deterioration
- Liquidity stress

---

## Risk Mitigation

- Collateral agreements
- Netting
- Central clearing
- Margin requirements
""")

    col1, col2 = st.columns(2)

    with col1:

        exposure = st.number_input(
            "Current Exposure",
            value=5000000.0
        )

        default_probability = st.number_input(
            "Default Probability (%)",
            value=3.0
        )

    with col2:

        recovery_rate = st.slider(
            "Recovery Rate (%)",
            0,
            100,
            40
        )

    loss_given_default = 1 - recovery_rate/100

    expected_loss = (
        exposure *
        default_probability/100 *
        loss_given_default
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Loss Given Default",
        pct(loss_given_default*100)
    )

    col2.metric(
        "Expected Credit Loss",
        currency(expected_loss)
    )

# =========================================================
# EXPOSURE PROFILE
# =========================================================

elif menu == "Exposure Profile":

    st.header("📈 Exposure Profile")

    periods = st.slider(
        "Number of Months",
        6,
        60,
        24
    )

    avg_exposure = st.number_input(
        "Average Exposure",
        value=2000000.0
    )

    volatility = st.number_input(
        "Exposure Volatility",
        value=700000.0
    )

    exposure_path = np.abs(
        np.random.normal(
            avg_exposure,
            volatility,
            periods
        )
    )

    exposure_df = pd.DataFrame({

        "Month": np.arange(1, periods+1),
        "Expected Exposure": exposure_path

    })

    st.dataframe(
        exposure_df,
        use_container_width=True
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=exposure_df["Month"],
        y=exposure_df["Expected Exposure"],
        mode='lines+markers'
    ))

    fig.update_layout(
        title="Expected Positive Exposure",
        xaxis_title="Month",
        yaxis_title="Exposure"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# COLLATERAL SIMULATION
# =========================================================

elif menu == "Collateral Simulation":

    st.header("🛡️ Collateral Simulation")

    col1, col2 = st.columns(2)

    with col1:

        exposure = st.number_input(
            "Exposure Amount",
            value=10000000.0
        )

        collateral = st.number_input(
            "Collateral Posted",
            value=6000000.0
        )

    with col2:

        haircut = st.slider(
            "Collateral Haircut (%)",
            0,
            50,
            10
        )

    effective_collateral = collateral * (
        1 - haircut/100
    )

    unsecured_exposure = max(
        0,
        exposure - effective_collateral
    )

    col1, col2 = st.columns(2)

    col1.metric(
        "Effective Collateral",
        currency(effective_collateral)
    )

    col2.metric(
        "Residual Exposure",
        currency(unsecured_exposure)
    )

# =========================================================
# CSA LOGIC
# =========================================================

elif menu == "CSA Logic":

    st.header("📜 CSA Logic")

    col1, col2 = st.columns(2)

    with col1:

        mtm = st.number_input(
            "Current MTM Exposure",
            value=12000000.0
        )

        threshold = st.number_input(
            "CSA Threshold",
            value=5000000.0
        )

    with col2:

        minimum_transfer = st.number_input(
            "Minimum Transfer Amount",
            value=1000000.0
        )

    collateral_call = max(
        0,
        mtm - threshold
    )

    if collateral_call < minimum_transfer:

        collateral_call = 0

    st.metric(
        "Collateral Call",
        currency(collateral_call)
    )

# =========================================================
# CENTRAL CLEARING
# =========================================================

elif menu == "Central Clearing":

    st.header("🏛️ Central Clearing")

    initial_margin = st.number_input(
        "Initial Margin",
        value=5000000.0
    )

    variation_margin = st.number_input(
        "Variation Margin",
        value=800000.0
    )

    total_margin = (
        initial_margin +
        variation_margin
    )

    st.metric(
        "Total Margin Requirement",
        currency(total_margin)
    )

# =========================================================
# CVA BASICS
# =========================================================

elif menu == "CVA Basics":

    st.header("📉 Credit Valuation Adjustment")

    col1, col2 = st.columns(2)

    with col1:

        exposure = st.number_input(
            "Expected Exposure",
            value=10000000.0
        )

        pd = st.number_input(
            "Default Probability (%)",
            value=2.5
        )

    with col2:

        lgd = st.number_input(
            "Loss Given Default (%)",
            value=60.0
        )

    cva = exposure * pd/100 * lgd/100

    st.metric(
        "Estimated CVA",
        currency(cva)
    )
# =========================================================
# CREDIT DEFAULT SWAPS (CDS)
# =========================================================

elif menu == "Credit Default Swaps":

    st.header("💳 Credit Default Swaps (CDS)")

    st.markdown("""

## What is a Credit Default Swap?

A CDS is a credit derivative contract.

It acts like insurance against:
- bond default
- loan default
- sovereign default

---

## Parties in CDS

### Protection Buyer
- pays CDS premium
- receives compensation if default occurs

### Protection Seller
- receives premium
- compensates buyer during credit event

---

## Common Credit Events

- Bankruptcy
- Failure to Pay
- Debt Restructuring
- Sovereign Default

---

## Applications

✅ Credit risk hedging  
✅ Speculation on credit quality  
✅ Bond spread trading  
✅ Counterparty risk management  
✅ Basel risk management

""")

    # =====================================================
    # INPUTS
    # =====================================================

    col1, col2 = st.columns(2)

    with col1:

        notional = st.number_input(
            "CDS Notional",
            value=10000000.0,
            key="cds_notional"
        )

        cds_spread = st.number_input(
            "CDS Spread (bps)",
            value=150.0,
            key="cds_spread"
        )

        maturity = st.number_input(
            "Maturity (Years)",
            value=5,
            key="cds_maturity"
        )

    with col2:

        recovery_rate = st.slider(
            "Recovery Rate (%)",
            0,
            100,
            40,
            key="cds_recovery"
        )

        default_probability = st.number_input(
            "Default Probability (%)",
            value=3.0,
            key="cds_pd"
        )

    # =====================================================
    # CALCULATIONS
    # =====================================================

    annual_premium = (
        notional *
        cds_spread / 10000
    )

    total_premium = (
        annual_premium *
        maturity
    )

    loss_given_default = (
        1 - recovery_rate/100
    )

    protection_payment = (
        notional *
        loss_given_default
    )

    expected_loss = (
        notional *
        default_probability/100 *
        loss_given_default
    )

    # =====================================================
    # OUTPUT METRICS
    # =====================================================

    st.subheader("📊 CDS Analytics")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Annual CDS Premium",
        currency(annual_premium)
    )

    col2.metric(
        "Protection Payment",
        currency(protection_payment)
    )

    col3.metric(
        "Expected Credit Loss",
        currency(expected_loss)
    )

    st.metric(
        "Total Premium Over Maturity",
        currency(total_premium)
    )

    # =====================================================
    # CDS CASH FLOW TABLE
    # =====================================================

    premium_schedule = []

    for year in range(1, maturity+1):

        premium_schedule.append({

            "Year": year,
            "Annual Premium": annual_premium

        })

    cds_df = pd.DataFrame(
        premium_schedule
    )

    st.subheader("📄 Premium Payment Schedule")

    st.dataframe(
        cds_df,
        use_container_width=True
    )

    # =====================================================
    # CDS VISUALIZATION
    # =====================================================

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=cds_df["Year"],
        y=cds_df["Annual Premium"],
        name="CDS Premium"
    ))

    fig.update_layout(
        title="CDS Premium Payments Through Time",
        xaxis_title="Year",
        yaxis_title="Premium Payment"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.subheader("🧠 Interpretation")

    if cds_spread < 100:

        st.success("""
Low CDS spread indicates relatively low perceived credit risk.
""")

    elif cds_spread < 300:

        st.warning("""
Moderate CDS spread indicates elevated credit risk.
""")

    else:

        st.error("""
High CDS spread indicates severe market concern regarding default risk.
""")

    # =====================================================
    # EDUCATIONAL NOTES
    # =====================================================

    st.markdown("""

---

## CDS Spread Interpretation

| CDS Spread | Credit Quality |
|---|---|
| <100 bps | Strong Credit |
| 100–300 bps | Moderate Risk |
| >300 bps | Distressed Credit |

---

## Important Insight

Higher CDS spreads imply:
- higher default probability
- worsening market perception
- increasing borrowing costs

CDS became globally important during:
- 2008 Financial Crisis
- Sovereign Debt Crises
- Banking Stress Episodes

""")
# =========================================================
# CDS SPREAD CALCULATOR
# =========================================================

elif menu == "CDS Spread Calculator":

    st.header("📈 CDS Spread Calculator")

    notional = st.number_input(
        "Bond Notional",
        value=10000000.0,
        key="cds_calc_notional"
    )

    annual_premium = st.number_input(
        "Annual CDS Premium",
        value=250000.0,
        key="cds_calc_premium"
    )

    cds_spread = (
        annual_premium / notional
    ) * 10000

    st.metric(
        "CDS Spread (bps)",
        round(cds_spread, 2)
    )

    if cds_spread < 100:

        st.success("Low Credit Risk")

    elif cds_spread < 300:

        st.warning("Moderate Credit Risk")

    else:

        st.error("High Credit Risk")    
# =========================================================
# CDS PAYOFF SIMULATOR
# =========================================================

elif menu == "CDS Payoff Simulator":

    st.header("💰 CDS Payoff Simulator")

    notional = st.number_input(
        "CDS Notional",
        value=10000000.0,
        key="cds_payoff_notional"
    )

    recovery = st.slider(
        "Recovery Rate (%)",
        0,
        100,
        40,
        key="cds_payoff_recovery"
    )

    default = st.checkbox(
        "Trigger Credit Event?"
    )

    if default:

        payoff = (
            notional *
            (1 - recovery/100)
        )

    else:

        payoff = 0

    st.metric(
        "CDS Protection Payment",
        currency(payoff)
    )
# =========================================================
# CDS VS BOND SPREAD
# =========================================================

elif menu == "CDS vs Bond Spread":

    st.header("⚖️ CDS vs Bond Spread")

    bond_yield = st.number_input(
        "Corporate Bond Yield (%)",
        value=9.0,
        key="bond_yield"
    )

    govt_yield = st.number_input(
        "Government Bond Yield (%)",
        value=7.0,
        key="govt_yield"
    )

    cds_spread = st.number_input(
        "CDS Spread (bps)",
        value=180.0,
        key="bond_cds_spread"
    )

    bond_spread = (
        bond_yield - govt_yield
    ) * 100

    col1, col2 = st.columns(2)

    col1.metric(
        "Bond Spread (bps)",
        round(bond_spread, 2)
    )

    col2.metric(
        "CDS Spread (bps)",
        cds_spread
    )

    spread_difference = cds_spread - bond_spread

    st.metric(
        "Basis Difference",
        round(spread_difference, 2)
    )
# =========================================================
# CREDIT EVENT SIMULATOR
# =========================================================

elif menu == "Credit Event Simulator":

    st.header("⚠️ Credit Event Simulator")

    entity = st.text_input(
        "Reference Entity",
        value="XYZ Corp"
    )

    event = st.selectbox(

        "Credit Event",

        [

            "Bankruptcy",
            "Failure to Pay",
            "Debt Restructuring",
            "Sovereign Default"

        ]
    )

    notional = st.number_input(
        "CDS Notional",
        value=10000000.0,
        key="credit_event_notional"
    )

    recovery = st.slider(
        "Recovery Rate (%)",
        0,
        100,
        35,
        key="credit_event_recovery"
    )

    payout = (
        notional *
        (1 - recovery/100)
    )

    st.error(f"""
Credit Event Triggered:
{event}
""")

    st.metric(
        "Protection Payment",
        currency(payout)
    )
# =========================================================
# SOVEREIGN CDS MONITOR
# =========================================================

elif menu == "Sovereign CDS Monitor":

    st.header("🌍 Sovereign CDS Monitor")

    sovereign_df = pd.DataFrame({

        "Country": [

            "USA",
            "India",
            "Brazil",
            "Turkey",
            "Argentina"

        ],

        "CDS Spread (bps)": [

            35,
            85,
            220,
            410,
            1200

        ]

    })

    st.dataframe(
        sovereign_df,
        use_container_width=True
    )

    fig = px.bar(

        sovereign_df,

        x="Country",

        y="CDS Spread (bps)",

        title="Sovereign CDS Risk"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# TREASURY DESK SIMULATOR
# =========================================================

elif menu == "Treasury Desk Simulator":

    st.header("🏢 Treasury Desk Simulator")

    debt_type = st.selectbox(

        "Debt Type",

        [
            "Floating Rate Debt",
            "Fixed Rate Debt"
        ]
    )

    market_view = st.selectbox(

        "Interest Rate Expectation",

        [
            "Rates Rising",
            "Rates Falling",
            "Rates Stable"
        ]
    )

    if debt_type == "Floating Rate Debt":

        if market_view == "Rates Rising":

            st.success("""
Recommended Strategy:

✅ Pay Fixed / Receive Floating IRS
""")

# =========================================================
# TREASURY ROLEPLAY
# =========================================================

elif menu == "Treasury Roleplay":

    st.header("🎯 Treasury Roleplay")

    hedge_interest = st.checkbox(
        "Use Interest Rate Swap"
    )

    hedge_fx = st.checkbox(
        "Use Currency Swap"
    )

    hedge_commodity = st.checkbox(
        "Use Commodity Swap"
    )

    score = 0

    if hedge_interest:
        score += 1

    if hedge_fx:
        score += 1

    if hedge_commodity:
        score += 1

    st.metric(
        "Treasury Hedge Score",
        f"{score}/3"
    )

# =========================================================
# HEDGE RECOMMENDATION ENGINE
# =========================================================

elif menu == "Hedge Recommendation Engine":

    st.header("🧠 Hedge Recommendation Engine")

    exposure = st.selectbox(

        "Primary Exposure",

        [
            "Floating Interest Rate",
            "FX Exposure",
            "Commodity Exposure"
        ]
    )

    market_view = st.selectbox(

        "Market Expectation",

        [
            "Rates Rising",
            "Rates Falling",
            "INR Depreciating",
            "Commodity Prices Rising"
        ]
    )

    if exposure == "Floating Interest Rate":

        if market_view == "Rates Rising":

            st.success("""
✅ Recommended:
Pay Fixed IRS
""")

# =========================================================
# MULTI-RISK TREASURY DASHBOARD
# =========================================================

elif menu == "Multi-Risk Treasury Dashboard":

    st.header("📊 Multi-Risk Treasury Dashboard")

    ir_exposure = st.number_input(
        "Interest Rate Exposure",
        value=200000000.0
    )

    fx_exposure = st.number_input(
        "FX Exposure",
        value=100000000.0
    )

    commodity_exposure = st.number_input(
        "Commodity Exposure",
        value=50000000.0
    )

    exposure_df = pd.DataFrame({

        "Risk Type": [
            "Interest Rate",
            "FX",
            "Commodity"
        ],

        "Exposure": [
            ir_exposure,
            fx_exposure,
            commodity_exposure
        ]
    })

    fig = px.pie(
        exposure_df,
        names="Risk Type",
        values="Exposure",
        title="Treasury Risk Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# ALM SIMULATOR
# =========================================================

elif menu == "ALM Simulator":

    st.header("🏦 Asset Liability Management")

    asset_duration = st.number_input(
        "Asset Duration",
        value=5.0
    )

    liability_duration = st.number_input(
        "Liability Duration",
        value=3.0
    )

    gap = asset_duration - liability_duration

    st.metric(
        "Duration Gap",
        round(gap, 2)
    )

# =========================================================
# MIFOR SWAPS
# =========================================================

elif menu == "MIFOR Swaps":

    st.header("🇮🇳 MIFOR Swaps")

    usd_rate = st.number_input(
        "USD Rate (%)",
        value=5.0
    )

    forward_premium = st.number_input(
        "Forward Premium (%)",
        value=2.0
    )

    spread = st.number_input(
        "Bank Spread (%)",
        value=0.5
    )

    mifor = usd_rate + forward_premium + spread

    st.metric(
        "MIFOR Rate",
        pct(mifor)
    )

# =========================================================
# INDIAN SWAPS MARKET
# =========================================================

elif menu == "Indian Swaps Market":

    st.header("🇮🇳 Indian Swaps Market")

    market_df = pd.DataFrame({

        "Product": [

            "Interest Rate Swaps",
            "OIS Swaps",
            "Currency Swaps",
            "MIFOR Swaps"

        ],

        "Primary Use": [

            "Interest-rate hedging",
            "Liquidity/rate expectations",
            "FX hedging",
            "Offshore borrowing"

        ]

    })

    st.table(market_df)

# =========================================================
# OIS SWAPS
# =========================================================

elif menu == "OIS Swaps":

    st.header("🏦 Overnight Indexed Swaps")

    fixed_rate = st.number_input(
        "Fixed OIS Rate (%)",
        value=6.5
    )

    overnight_rate = st.number_input(
        "Expected Overnight Rate (%)",
        value=6.2
    )

    spread = fixed_rate - overnight_rate

    st.metric(
        "OIS Spread",
        pct(spread)
    )

# =========================================================
# BENCHMARK TRANSITION
# =========================================================

elif menu == "Benchmark Transition":

    st.header("🔄 LIBOR to SOFR Transition")

    old_rate = st.number_input(
        "Old LIBOR Rate (%)",
        value=5.5
    )

    spread_adjustment = st.number_input(
        "Spread Adjustment (%)",
        value=0.30
    )

    sofr = st.number_input(
        "SOFR (%)",
        value=5.1
    )

    adjusted_rate = sofr + spread_adjustment

    col1, col2 = st.columns(2)

    col1.metric(
        "Legacy LIBOR",
        pct(old_rate)
    )

    col2.metric(
        "SOFR Equivalent",
        pct(adjusted_rate)
    )

# =========================================================
# SWAP TIMELINE VISUALIZER
# =========================================================

elif menu == "Swap Timeline Visualizer":

    st.header("📅 Swap Timeline Visualizer")

    years = st.slider(
        "Swap Tenure",
        1,
        10,
        5
    )

    periods = np.arange(
        0,
        years+1
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=periods,
        y=[1]*len(periods),
        mode='lines+markers+text',
        text=[f"T{i}" for i in periods]
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# SWAPS VS FUTURES VS FORWARDS
# =========================================================

elif menu == "Swaps vs Futures vs Forwards":

    st.header("⚖️ Swaps vs Futures vs Forwards")

    comparison_df = pd.DataFrame({

        "Feature": [

            "Trading Venue",
            "Standardisation",
            "Counterparty Risk",
            "Liquidity"

        ],

        "Swaps": [

            "OTC",
            "Custom",
            "High",
            "Moderate"

        ],

        "Futures": [

            "Exchange",
            "Standardized",
            "Low",
            "High"

        ],

        "Forwards": [

            "OTC",
            "Custom",
            "High",
            "Low"

        ]

    })

    st.table(comparison_df)
# =========================================================
# CASE-BASED LEARNING
# =========================================================

elif menu == "Case-Based Learning":

    st.header("📚 Case-Based Learning")

    case = st.selectbox(

        "Choose Case Study",

        [

            "Airline Fuel Hedge",
            "IT Exporter Currency Risk",
            "Infrastructure Floating Debt",
            "Bank ALM Management",
            "Oil Refinery Commodity Hedge"

        ]
    )

    if case == "Airline Fuel Hedge":

        st.subheader("✈️ Airline Fuel Hedge")

        st.markdown("""
### Situation

An airline fears:
- rising crude oil prices
- volatile jet fuel costs

### Hedge Strategy

✅ Commodity Swap

Result:
- stabilized fuel costs
- reduced earnings volatility
""")

    elif case == "IT Exporter Currency Risk":

        st.subheader("💱 IT Exporter FX Risk")

        st.markdown("""
### Situation

Indian IT exporter:
- earns USD revenue
- reports in INR

### Hedge Strategy

✅ Currency Swap

Result:
- stable INR cash flows
""")

# =========================================================
# STEP-BY-STEP SOLVER
# =========================================================

elif menu == "Step-by-Step Solver":

    st.header("🧠 Step-by-Step Solver")

    principal = st.number_input(
        "Principal",
        value=10000000.0
    )

    fixed = st.number_input(
        "Fixed Rate (%)",
        value=7.0
    )

    floating = st.number_input(
        "Floating Rate (%)",
        value=6.4
    )

    st.subheader("Step 1 — Fixed Leg")

    fixed_cf = principal * fixed/100

    st.write(
        f"Fixed Cash Flow = {currency(fixed_cf)}"
    )

    st.subheader("Step 2 — Floating Leg")

    floating_cf = principal * floating/100

    st.write(
        f"Floating Cash Flow = {currency(floating_cf)}"
    )

    settlement = floating_cf - fixed_cf

    st.subheader("Step 3 — Net Settlement")

    st.success(
        f"Net Settlement = {currency(settlement)}"
    )

# =========================================================
# QUIZ ENGINE
# =========================================================

elif menu == "Quiz Engine":

    st.header("🧠 Quiz Engine")

    questions = [

        {

            "q": "Which swap exchanges fixed and floating interest?",

            "options": [

                "Currency Swap",
                "Interest Rate Swap",
                "Commodity Swap"

            ],

            "answer": "Interest Rate Swap"

        },

        {

            "q": "Which benchmark replaced LIBOR?",

            "options": [

                "SOFR",
                "MIBOR",
                "TREPS"

            ],

            "answer": "SOFR"

        }

    ]

    score = 0

    for i, q in enumerate(questions):

        st.subheader(f"Question {i+1}")

        ans = st.radio(
            q["q"],
            q["options"],
            key=f"quiz_{i}"
        )

        if ans == q["answer"]:

            score += 1

    st.metric(
        "Quiz Score",
        f"{score}/{len(questions)}"
    )

# =========================================================
# FORMULA SHEET
# =========================================================

elif menu == "Formula Cheat Sheet":

    st.header("📄 Formula Cheat Sheet")

    st.markdown("""
## Swap Value

Swap Value = PV(Floating Leg) − PV(Fixed Leg)

---

## Discount Factor

DF = 1 / (1+r)^t

---

## DV01

DV01 = MV × Duration × 0.0001

---

## CVA

CVA ≈ Exposure × PD × LGD
""")

# =========================================================
# COMMON STUDENT MISTAKES
# =========================================================

elif menu == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes")

    mistakes_df = pd.DataFrame({

        "Mistake": [

            "Ignoring discounting",
            "Confusing swaps with forwards",
            "Wrong principal exchange logic",
            "Ignoring duration risk"

        ],

        "Correction": [

            "Discount future cash flows",
            "Swaps involve periodic exchanges",
            "Currency swaps exchange principal",
            "Understand DV01 and duration"

        ]

    })

    st.table(mistakes_df)

# =========================================================
# SWAPTIONS
# =========================================================

elif menu == "Swaptions":

    st.header("🎯 Swaptions")

    swaption_type = st.selectbox(

        "Swaption Type",

        [
            "Payer Swaption",
            "Receiver Swaption"
        ]
    )

    notional = st.number_input(
        "Notional",
        value=10000000.0
    )

    intrinsic = st.number_input(
        "Intrinsic Value",
        value=350000.0
    )

    premium = st.number_input(
        "Premium",
        value=120000.0
    )

    payoff = intrinsic - premium

    st.metric(
        "Net Swaption Payoff",
        currency(payoff)
    )

# =========================================================
# ADVANCED CVA
# =========================================================

elif menu == "Advanced CVA":

    st.header("📉 Advanced CVA")

    periods = st.slider(
        "Exposure Periods",
        5,
        30,
        12
    )

    exposure = np.abs(
        np.random.normal(
            2000000,
            500000,
            periods
        )
    )

    default_probs = np.linspace(
        0.01,
        0.05,
        periods
    )

    recovery = st.slider(
        "Recovery Rate (%)",
        0,
        100,
        40
    )

    lgd = 1 - recovery/100

    cva_values = exposure * default_probs * lgd

    total_cva = np.sum(cva_values)

    cva_df = pd.DataFrame({

        "Period": np.arange(1, periods+1),
        "Exposure": exposure,
        "PD": default_probs,
        "CVA": cva_values

    })

    st.dataframe(
        cva_df,
        use_container_width=True
    )

    st.metric(
        "Total CVA",
        currency(total_cva)
    )

# =========================================================
# XVA OVERVIEW
# =========================================================

elif menu == "XVA Overview":

    st.header("📚 XVA Overview")

    xva_df = pd.DataFrame({

        "Type": [

            "CVA",
            "DVA",
            "FVA",
            "MVA",
            "KVA"

        ],

        "Meaning": [

            "Credit Adjustment",
            "Debit Adjustment",
            "Funding Adjustment",
            "Margin Adjustment",
            "Capital Adjustment"

        ]

    })

    st.table(xva_df)

# =========================================================
# MONTE CARLO RATE SIMULATION
# =========================================================

elif menu == "Monte Carlo Rate Simulation":

    st.header("🎲 Monte Carlo Rate Simulation")

    periods = st.slider(
        "Simulation Periods",
        12,
        120,
        36
    )

    simulations = st.slider(
        "Number of Simulations",
        10,
        300,
        100
    )

    initial_rate = st.number_input(
        "Initial Rate (%)",
        value=6.5
    )

    volatility = st.number_input(
        "Volatility",
        value=0.02
    )

    paths = []

    for s in range(simulations):

        rates = [initial_rate]

        for t in range(periods):

            shock = np.random.normal(
                0,
                volatility
            )

            rates.append(
                rates[-1] + shock
            )

        paths.append(rates)

    fig = go.Figure()

    for i in range(min(20, simulations)):

        fig.add_trace(go.Scatter(
            y=paths[i],
            mode='lines',
            opacity=0.4,
            showlegend=False
        ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# HEDGE EFFECTIVENESS
# =========================================================

elif menu == "Hedge Effectiveness":

    st.header("🛡️ Hedge Effectiveness")

    exposure_change = st.number_input(
        "Exposure Change",
        value=-5000000.0
    )

    hedge_change = st.number_input(
        "Hedge Value Change",
        value=4500000.0
    )

    effectiveness = abs(
        hedge_change / exposure_change
    ) * 100

    st.metric(
        "Hedge Effectiveness",
        pct(effectiveness)
    )

# =========================================================
# HEDGE ACCOUNTING
# =========================================================

elif menu == "Hedge Accounting":

    st.header("📒 Hedge Accounting")

    hedge_type = st.selectbox(

        "Hedge Type",

        [

            "Fair Value Hedge",
            "Cash Flow Hedge",
            "Net Investment Hedge"

        ]
    )

    st.info(f"""
Selected:
{hedge_type}
""")

# =========================================================
# PORTFOLIO SWAP ANALYTICS
# =========================================================

elif menu == "Portfolio Swap Analytics":

    st.header("📊 Portfolio Swap Analytics")

    n_swaps = st.slider(
        "Number of Swaps",
        1,
        20,
        5
    )

    values = np.random.normal(
        10000000,
        3000000,
        n_swaps
    )

    durations = np.random.normal(
        4,
        1,
        n_swaps
    )

    portfolio_df = pd.DataFrame({

        "Swap": [
            f"Swap {i+1}"
            for i in range(n_swaps)
        ],

        "Market Value": values,
        "Duration": durations

    })

    st.dataframe(
        portfolio_df,
        use_container_width=True
    )

# =========================================================
# SWAPTION PAYOFF VISUALIZER
# =========================================================

elif menu == "Swaption Payoff Visualizer":

    st.header("📈 Swaption Payoff Visualizer")

    strike = st.number_input(
        "Strike Rate (%)",
        value=7.0
    )

    market_rates = np.arange(
        3,
        12,
        0.25
    )

    payer_payoff = np.maximum(
        market_rates - strike,
        0
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=market_rates,
        y=payer_payoff,
        mode='lines'
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# TREASURY WAR ROOM
# =========================================================

elif menu == "Treasury War Room":

    st.header("🚨 Treasury War Room")

    rate_shock = st.slider(
        "Interest Rate Shock",
        0,
        500,
        200
    )

    fx_shock = st.slider(
        "FX Shock",
        0,
        30,
        10
    )

    oil_shock = st.slider(
        "Oil Shock",
        0,
        50,
        20
    )

    total_risk = (
        rate_shock +
        fx_shock +
        oil_shock
    )

    st.metric(
        "Treasury Risk Score",
        total_risk
    )

# =========================================================
# LIVE STRATEGY ENGINE
# =========================================================

elif menu == "Live Strategy Engine":

    st.header("🧠 Live Strategy Engine")

    environment = st.selectbox(

        "Market Environment",

        [

            "Rates Rising",
            "Rates Falling",
            "FX Volatility",
            "Commodity Supercycle"

        ]
    )

    if environment == "Rates Rising":

        st.success("""
✅ Use Pay-Fixed IRS
""")

# =========================================================
# GAMIFIED LEARNING
# =========================================================

elif menu == "Gamified Learning":

    st.header("🎮 Gamified Learning")

    tasks = {

        "IRS Module": False,
        "Treasury Simulation": False,
        "Valuation Module": False

    }

    completed = 0

    for task in tasks:

        done = st.checkbox(task)

        if done:
            completed += 1

    progress = completed / len(tasks) * 100

    st.progress(progress/100)

    st.metric(
        "Completion",
        pct(progress)
    )

# =========================================================
# FACULTY MODE
# =========================================================

elif menu == "Faculty Mode":

    st.header("👨‍🏫 Faculty Mode")

    topic = st.selectbox(

        "Teaching Topic",

        [

            "IRS",
            "Currency Swaps",
            "Swap Valuation",
            "Treasury Management"

        ]
    )

    st.info(f"""
Suggested classroom activity for:
{topic}
""")

# =========================================================
# EXECUTIVE EDUCATION MODE
# =========================================================

elif menu == "Executive Education Mode":

    st.header("🏢 Executive Education Mode")

    participant = st.selectbox(

        "Participant Type",

        [

            "Corporate Treasurer",
            "Bank Treasury",
            "Risk Manager",
            "CFO"

        ]
    )

    st.success(f"""
Customized learning path for:
{participant}
""")

# =========================================================
# TREASURY SCORECARD
# =========================================================

elif menu == "Treasury Scorecard":

    st.header("📋 Treasury Scorecard")

    hedge = st.slider(
        "Hedging Effectiveness",
        0,
        100,
        75
    )

    liquidity = st.slider(
        "Liquidity Management",
        0,
        100,
        70
    )

    duration = st.slider(
        "Duration Management",
        0,
        100,
        80
    )

    overall = np.mean([
        hedge,
        liquidity,
        duration
    ])

    st.metric(
        "Overall Treasury Score",
        round(overall, 2)
    )

# =========================================================
# CAPSTONE SIMULATION
# =========================================================

elif menu == "Capstone Simulation":

    st.header("🎓 Capstone Simulation")

    ir_risk = st.slider(
        "Interest Rate Risk",
        0,
        100,
        70
    )

    fx_risk = st.slider(
        "FX Risk",
        0,
        100,
        60
    )

    commodity_risk = st.slider(
        "Commodity Risk",
        0,
        100,
        50
    )

    hedge_ratio = st.slider(
        "Hedge Ratio",
        0,
        100,
        75
    )

    residual = (
        ir_risk +
        fx_risk +
        commodity_risk
    ) * (1 - hedge_ratio/100)

    st.metric(
        "Residual Risk",
        round(residual, 2)
    )

# =========================================================
# LEARNING PROGRESS TRACKER
# =========================================================

elif menu == "Learning Progress Tracker":

    st.header("📚 Progress Tracker")

    modules = [

        "IRS",
        "Currency Swaps",
        "Valuation",
        "Risk Management"

    ]

    completed = st.multiselect(
        "Completed Modules",
        modules
    )

    progress = (
        len(completed) / len(modules)
    ) * 100

    st.progress(progress/100)

# =========================================================
# BADGE SYSTEM
# =========================================================

elif menu == "Badge System":

    st.header("🏅 Badge System")

    score = st.slider(
        "Quiz Score",
        0,
        100,
        75
    )

    if score >= 90:

        st.success("""
🏆 Treasury Expert Badge
""")

# =========================================================
# INTERACTIVE TIMELINE ENGINE
# =========================================================

elif menu == "Interactive Timeline Engine":

    st.header("📅 Interactive Timeline")

    years = st.slider(
        "Swap Tenure",
        1,
        10,
        5
    )

    timeline = np.arange(
        0,
        years+1
    )

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=timeline,
        y=[1]*len(timeline),
        mode='lines+markers+text',
        text=[f"T{i}" for i in timeline]
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# SWAP DASHBOARD
# =========================================================

elif menu == "Swap Dashboard":

    st.header("📊 Swap Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Portfolio MTM",
        currency(25000000)
    )

    col2.metric(
        "DV01",
        currency(175000)
    )

    col3.metric(
        "CVA",
        currency(2400000)
    )

# =========================================================
# SWAP MARKET SIMULATOR
# =========================================================

elif menu == "Swap Market Simulator":

    st.header("🌍 Swap Market Simulator")

    periods = st.slider(
        "Simulation Periods",
        10,
        100,
        30
    )

    base_rate = st.number_input(
        "Initial Rate",
        value=6.5
    )

    simulated_rates = [base_rate]

    for i in range(periods):

        simulated_rates.append(
            simulated_rates[-1] +
            np.random.normal(0,0.15)
        )

    fig = px.line(
        y=simulated_rates
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# =========================================================
# REPORT GENERATOR
# =========================================================

elif menu == "Report Generator":

    st.header("📄 Report Generator")

    company = st.text_input(
        "Company Name",
        value="ABC Infrastructure Ltd."
    )

    report = f"""
SWAP ANALYTICS REPORT

Company:
{company}

Key Metrics:
- Portfolio MTM
- DV01
- CVA
"""

    st.download_button(

        label="Download Report",

        data=report,

        file_name="swap_report.txt"

    )

# =========================================================
# CERTIFICATE GENERATOR
# =========================================================

elif menu == "Certificate Generator":

    st.header("🎓 Certificate Generator")

    student = st.text_input(
        "Student Name"
    )

    certificate = f"""
Certificate awarded to:
{student}
"""

    st.download_button(

        label="Download Certificate",

        data=certificate,

        file_name="certificate.txt"

    )

# =========================================================
# FINANCE UI ENHANCEMENTS
# =========================================================

elif menu == "Finance UI Enhancements":

    st.header("🎨 Finance UI Enhancements")

    st.code("""

st.markdown(
    '''
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    </style>
    ''',
    unsafe_allow_html=True
)

""")
