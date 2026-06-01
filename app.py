import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import norm
import random

st.set_page_config(
    page_title="Swaps Learning Lab",
    page_icon="🔄",
    layout="wide"
)

# =========================================================
# Helper Functions
# =========================================================

def currency(x):
    return f"₹{x:,.2f}"

def pct(x, d=2):
    return f"{round(x, d)}%"

# =========================================================
# TITLE
# =========================================================

st.title("🔄 Experiential Learning Lab — Swaps")

st.markdown("""
Welcome to the **Swaps Learning Platform**.

This app covers:

- Introduction to Swaps
- Interest Rate Swaps (IRS)
- Currency Swaps
- Commodity Swaps
- Equity Swaps
- Comparative Advantage Theory
- Swap Cash Flows
- Swap Pricing & Valuation
- Mark-to-Market
- Swap Curves
- OIS Swaps
- Counterparty Risk
- Treasury Risk Management
- Indian Swaps Market
- Case-Based Learning
- Quiz Engine
- Formula Cheat Sheet

through:

✅ Interactive calculators  
✅ Treasury simulations  
✅ Timeline diagrams  
✅ Real-world examples  
✅ Step-by-step valuation  
✅ Visual learning  
✅ Indian market applications  
""")

# =========================================================
# SIDEBAR MENU
# =========================================================

menu = st.sidebar.radio("Choose Module", [

    "Introduction to Swaps",
    "Interest Rate Swaps",
    "Currency Swaps",
    "Commodity Swaps",
    "Equity Swaps",
    "Comparative Advantage",
    "Swap Cash Flow Simulator",
    "Swap Pricing & Valuation",
    "Mark-to-Market",
    "OIS Swaps",
    "Swap Curve & Yield Curve",
    "Counterparty Risk",
    "Treasury Desk Simulator",
    "Indian Swaps Market",
    "Swaps vs Futures vs Forwards",
    "Case-Based Learning",
    "Quiz Engine",
    "Formula Cheat Sheet",
    "Common Student Mistakes"

])

# =========================================================
# INTRODUCTION
# =========================================================

if menu == "Introduction to Swaps":

    st.header("📘 Introduction to Swaps")

    st.markdown("""
## What is a Swap?

A **swap** is an OTC derivative contract in which two parties exchange
cash flows over time.

The cash flows are based on:
- interest rates
- currencies
- commodities
- equity returns

---

## Major Types of Swaps

| Swap Type | Exchange |
|---|---|
| Interest Rate Swap | Fixed ↔ Floating Interest |
| Currency Swap | Currency cash flows |
| Commodity Swap | Fixed ↔ Commodity price |
| Equity Swap | Equity return ↔ Fixed/Floating |

---

## Key Characteristics

| Feature | Swaps |
|---|---|
| OTC contract | Yes |
| Customisable | Highly |
| Counterparty risk | Present |
| Long maturity | Common |
| Intermediary | Usually bank/dealer |

---

## Why Use Swaps?

### Hedging
- Reduce interest rate risk
- Hedge currency exposure
- Stabilise cash flows

### Speculation
- Bet on rates or currencies

### Cost Reduction
- Comparative borrowing advantage

### Asset-Liability Management
- Treasury risk management
""")

    st.info("""
Example:
A company with floating-rate debt may enter into a swap
to convert floating payments into fixed payments.
""")

# =========================================================
# INTEREST RATE SWAPS
# =========================================================

elif menu == "Interest Rate Swaps":

    st.header("📈 Interest Rate Swaps (IRS)")

    st.markdown("""
## Plain Vanilla Interest Rate Swap

One party:
- pays FIXED
- receives FLOATING

Other party:
- pays FLOATING
- receives FIXED

No principal exchange occurs.

---

## Swap Payment Formula

### Fixed Leg:
""")

    :contentReference[oaicite:0]{index=0}

    st.markdown("""
### Floating Leg:
""")

    :contentReference[oaicite:1]{index=1}

    col1, col2 = st.columns(2)

    with col1:
        principal = st.number_input("Notional Principal (₹)", value=10000000.0)
        fixed_rate = st.number_input("Fixed Rate (%)", value=7.5)
        floating_rate = st.number_input("Floating Rate (%)", value=6.8)

    with col2:
        years = st.number_input("Swap Tenure (Years)", value=5)
        payments = st.selectbox("Payments per Year", [1, 2, 4])

    dt = 1 / payments

    fixed_payment = principal * fixed_rate/100 * dt
    floating_payment = principal * floating_rate/100 * dt
    net_payment = fixed_payment - floating_payment

    col1, col2, col3 = st.columns(3)

    col1.metric("Fixed Leg Payment", currency(fixed_payment))
    col2.metric("Floating Leg Payment", currency(floating_payment))
    col3.metric("Net Settlement", currency(net_payment))

    st.subheader("📅 Swap Timeline")

    periods = np.arange(1, years * payments + 1)

    df = pd.DataFrame({
        "Period": periods,
        "Fixed Payment": [fixed_payment]*len(periods),
        "Floating Payment": [floating_payment]*len(periods),
        "Net Payment": [net_payment]*len(periods)
    })

    st.dataframe(df)

    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df["Period"],
        y=df["Net Payment"],
        name="Net Settlement"
    ))

    fig.update_layout(
        title="IRS Net Settlement Through Time",
        xaxis_title="Payment Period",
        yaxis_title="Net Cash Flow"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# CURRENCY SWAPS
# =========================================================

elif menu == "Currency Swaps":

    st.header("💱 Currency Swaps")

    st.markdown("""
## Currency Swap Structure

In a currency swap:
- principal is exchanged
- interest payments are exchanged
- principal re-exchanged at maturity

Example:
- INR borrower
- USD borrower

Both firms obtain cheaper borrowing through swap arrangement.
""")

    col1, col2 = st.columns(2)

    with col1:
        inr_principal = st.number_input("INR Principal", value=100000000.0)
        usd_principal = st.number_input("USD Principal", value=1200000.0)

        inr_rate = st.number_input("INR Interest Rate (%)", value=7.0)
        usd_rate = st.number_input("USD Interest Rate (%)", value=5.0)

    with col2:
        fx_rate = st.number_input("Spot FX Rate (₹/$)", value=83.5)
        maturity = st.number_input("Years", value=3)

    inr_interest = inr_principal * inr_rate/100
    usd_interest = usd_principal * usd_rate/100

    col1, col2 = st.columns(2)

    col1.metric("Annual INR Interest", currency(inr_interest))
    col2.metric("Annual USD Interest", f"${usd_interest:,.2f}")

    st.subheader("🔁 Principal Exchange Timeline")

    timeline = pd.DataFrame({
        "Time": ["Start", "Annual Interest", "Maturity"],
        "Cash Flow": [
            "Exchange Principals",
            "Exchange Interest Payments",
            "Re-exchange Principals"
        ]
    })

    st.table(timeline)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=[0, maturity],
        y=[inr_principal, -inr_principal],
        mode='lines+markers',
        name='INR Principal'
    ))

    fig.update_layout(
        title="Currency Swap Principal Exchange",
        xaxis_title="Years",
        yaxis_title="Cash Flow"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# COMPARATIVE ADVANTAGE
# =========================================================

elif menu == "Comparative Advantage":

    st.header("⚖️ Comparative Advantage in Swaps")

    st.markdown("""
## Why Swaps Exist

Swaps often arise because firms have different borrowing advantages.

Example:
- Company A better at fixed borrowing
- Company B better at floating borrowing

Both firms can benefit through swap arrangement.

---

## Total Gain Formula
""")

    :contentReference[oaicite:2]{index=2}

    col1, col2 = st.columns(2)

    with col1:
        a_fixed = st.number_input("Company A Fixed (%)", value=7.0)
        a_float = st.number_input("Company A Floating (%)", value=LIBOR := 6.0)

    with col2:
        b_fixed = st.number_input("Company B Fixed (%)", value=9.0)
        b_float = st.number_input("Company B Floating (%)", value=7.5)

    fixed_diff = b_fixed - a_fixed
    float_diff = b_float - a_float

    total_gain = fixed_diff - float_diff

    col1, col2, col3 = st.columns(3)

    col1.metric("Fixed Market Spread", pct(fixed_diff))
    col2.metric("Floating Market Spread", pct(float_diff))
    col3.metric("Total Potential Gain", pct(total_gain))

    if total_gain > 0:
        st.success("✅ Swap creates comparative advantage gains.")
    else:
        st.warning("⚠️ No comparative advantage benefit.")

# =========================================================
# SWAP VALUATION
# =========================================================

elif menu == "Swap Pricing & Valuation":

    st.header("💰 Swap Pricing & Valuation")

    st.markdown("""
## Value of Interest Rate Swap

At initiation:
- swap value ≈ zero

Later:
- value changes as interest rates change

---

## Swap Value
""")

    :contentReference[oaicite:3]{index=3}

    col1, col2 = st.columns(2)

    with col1:
        fixed_leg = st.number_input("PV of Fixed Leg", value=9800000.0)
        floating_leg = st.number_input("PV of Floating Leg", value=10050000.0)

    with col2:
        side = st.radio("Position", ["Pay Fixed", "Receive Fixed"])

    if side == "Pay Fixed":
        value = floating_leg - fixed_leg
    else:
        value = fixed_leg - floating_leg

    st.metric("Swap Market Value", currency(value))

    if value > 0:
        st.success("Swap has positive value.")
    else:
        st.warning("Swap has negative value.")

# =========================================================
# MARK TO MARKET
# =========================================================

elif menu == "Mark-to-Market":

    st.header("📊 Mark-to-Market of Swaps")

    st.markdown("""
Swap values fluctuate with:
- interest rates
- yield curves
- counterparty spreads
- FX movements
""")

    periods = 12

    mtm_values = np.random.normal(0, 200000, periods).cumsum()

    df = pd.DataFrame({
        "Month": np.arange(1, periods+1),
        "Swap MTM": mtm_values
    })

    st.dataframe(df)

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=df["Month"],
        y=df["Swap MTM"],
        mode='lines+markers'
    ))

    fig.update_layout(
        title="Swap MTM Evolution",
        xaxis_title="Month",
        yaxis_title="Market Value"
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# OIS SWAPS
# =========================================================

elif menu == "OIS Swaps":

    st.header("🏦 Overnight Indexed Swaps (OIS)")

    st.markdown("""
## What is an OIS?

An Overnight Indexed Swap exchanges:
- fixed interest
- overnight compounded floating rate

In India:
- linked to MIBOR
- important for liquidity management
- used heavily by banks

---

## OIS Applications

- Monetary policy expectations
- Interest rate hedging
- Yield curve construction
""")

    fixed_ois = st.number_input("Fixed OIS Rate (%)", value=6.5)
    floating_ois = st.number_input("Expected Overnight Rate (%)", value=6.2)

    spread = fixed_ois - floating_ois

    st.metric("OIS Spread", pct(spread))

# =========================================================
# TREASURY DESK
# =========================================================

elif menu == "Treasury Desk Simulator":

    st.header("🏢 Treasury Desk Simulator")

    st.markdown("""
You are the corporate treasurer.

Your company has:
- floating-rate debt
- FX exposure
- interest-rate risk

Choose a hedge strategy.
""")

    exposure = st.selectbox(
        "Exposure Type",
        [
            "Floating Rate Loan",
            "USD Payable",
            "Commodity Purchase"
        ]
    )

    market_view = st.selectbox(
        "Market Expectation",
        [
            "Interest Rates Rising",
            "Interest Rates Falling",
            "INR Appreciating",
            "INR Depreciating"
        ]
    )

    if exposure == "Floating Rate Loan":

        if "Rising" in market_view:
            st.success("""
Recommended:
✅ Pay Fixed / Receive Floating Interest Rate Swap

Reason:
Lock borrowing cost before rates rise.
""")
        else:
            st.info("""
Recommended:
Remain floating or receive fixed.
""")

    elif exposure == "USD Payable":

        if "Depreciating" in market_view:
            st.success("""
Recommended:
Currency Swap or Forward Hedge
""")
        else:
            st.info("""
FX hedge may not be immediately necessary.
""")

# =========================================================
# INDIAN SWAPS MARKET
# =========================================================

elif menu == "Indian Swaps Market":

    st.header("🇮🇳 Indian Swaps Market")

    st.markdown("""
## Indian Interest Rate Swap Market

Major participants:
- Banks
- NBFCs
- Corporates
- Mutual funds

Regulators:
- RBI
- SEBI

Benchmarks:
- MIBOR
- TREPS
- Government bond yields

---

## Common Products

| Product | Usage |
|---|---|
| IRS | Interest hedging |
| OIS | Liquidity & rates |
| Currency Swaps | FX hedging |
| MIFOR Swaps | Offshore borrowing |

---

## MIFOR

Mumbai Interbank Forward Offer Rate:
- combines LIBOR + forward premium
- widely used in external commercial borrowing
""")

# =========================================================
# COMPARISON
# =========================================================

elif menu == "Swaps vs Futures vs Forwards":

    st.header("⚖️ Swaps vs Futures vs Forwards")

    df_compare = pd.DataFrame({

        "Feature": [
            "Trading Venue",
            "Standardisation",
            "Counterparty Risk",
            "Customisation",
            "Liquidity",
            "Typical Use"
        ],

        "Swaps": [
            "OTC",
            "Custom",
            "High",
            "Very High",
            "Moderate",
            "Long-term hedging"
        ],

        "Futures": [
            "Exchange",
            "Standardised",
            "Low",
            "Low",
            "High",
            "Trading & hedging"
        ],

        "Forwards": [
            "OTC",
            "Custom",
            "High",
            "Very High",
            "Low",
            "Corporate hedging"
        ]
    })

    st.table(df_compare)

# =========================================================
# CASE BASED LEARNING
# =========================================================

elif menu == "Case-Based Learning":

    st.header("📚 Case-Based Learning")

    case = st.selectbox(
        "Choose Case",
        [
            "Airline Fuel Hedge",
            "IT Exporter Currency Exposure",
            "Bank Interest Rate Risk"
        ]
    )

    if case == "Airline Fuel Hedge":

        st.info("""
An airline fears rising crude oil prices.

Solution:
Commodity swap locking fixed fuel price.

Result:
Stable operating costs.
""")

    elif case == "IT Exporter Currency Exposure":

        st.info("""
An Indian exporter receives USD revenues.

Risk:
INR appreciation reduces INR revenue.

Solution:
Currency swap / forward hedge.
""")

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
                "Commodity Swap",
                "Equity Swap"
            ],
            "answer": "Interest Rate Swap"
        },

        {
            "q": "Which swap usually exchanges principal amounts?",
            "options": [
                "IRS",
                "Commodity Swap",
                "Currency Swap",
                "Equity Swap"
            ],
            "answer": "Currency Swap"
        }

    ]

    score = 0

    for i, q in enumerate(questions):

        st.subheader(f"Question {i+1}")

        ans = st.radio(
            q["q"],
            q["options"],
            key=i
        )

        if ans == q["answer"]:
            score += 1

    st.metric("Your Score", f"{score}/{len(questions)}")

# =========================================================
# FORMULA CHEAT SHEET
# =========================================================

elif menu == "Formula Cheat Sheet":

    st.header("📄 Formula Cheat Sheet")

    st.markdown("""
## Key Swap Formulas
""")

    :contentReference[oaicite:4]{index=4}

    :contentReference[oaicite:5]{index=5}

    :contentReference[oaicite:6]{index=6}

# =========================================================
# COMMON STUDENT MISTAKES
# =========================================================

elif menu == "Common Student Mistakes":

    st.header("⚠️ Common Student Mistakes")

    mistakes = pd.DataFrame({

        "Mistake": [

            "Confusing fixed payer vs floating payer",
            "Ignoring net settlement",
            "Forgetting time value discounting",
            "Wrong principal exchange logic",
            "Confusing forwards with swaps"

        ],

        "Correction": [

            "Draw cash flow timeline",
            "Only net amount exchanged in IRS",
            "Discount future cash flows properly",
            "Currency swaps exchange principal",
            "Swaps involve multiple payments"

        ]
    })

    st.table(mistakes)
