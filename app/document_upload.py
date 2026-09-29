import streamlit as st
from pathlib import Path
from datetime import datetime
import numpy as np

st.set_page_config(
    page_title="SynthGigCredit",
    page_icon="◐",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = BASE_DIR / "data" / "applications"
DATA_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #F4F8FB 0%, #EEF5F7 50%, #F8FAFC 100%);
    color: #172033;
}

.block-container {
    max-width: 1150px;
    padding: 45px 55px 60px 55px;
}

h1, h2, h3 {
    color: #102A43 !important;
}

h1 {
    font-size: 46px !important;
    font-weight: 750 !important;
    letter-spacing: -1.5px;
    margin-bottom: 5px;
}

.subtitle {
    color: #526477;
    font-size: 18px;
    margin-bottom: 35px;
}

.card {
    background: #FFFFFF;
    border: 1px solid #D9E4EC;
    border-radius: 18px;
    padding: 26px 28px;
    margin-bottom: 22px;
    box-shadow: 0 5px 18px rgba(16, 42, 67, 0.06);
}

.section-title {
    color: #102A43;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 7px;
}

.small {
    color: #627487;
    font-size: 14px;
    line-height: 1.6;
}

label {
    color: #263B53 !important;
    font-weight: 600 !important;
}

div[data-baseweb="input"] {
    background-color: #FFFFFF;
    border: 1px solid #C9D7E2;
    border-radius: 10px;
}

div[data-baseweb="input"]:focus-within {
    border: 1px solid #159A9C;
    box-shadow: 0 0 0 2px rgba(21, 154, 156, 0.12);
}

div[data-baseweb="select"] > div {
    background-color: #FFFFFF;
    border: 1px solid #C9D7E2;
    border-radius: 10px;
}

.stButton > button {
    background: linear-gradient(135deg, #102A43, #159A9C);
    color: #FFFFFF;
    border: none;
    border-radius: 11px;
    padding: 13px 26px;
    font-size: 16px;
    font-weight: 700;
    box-shadow: 0 5px 14px rgba(16, 42, 67, 0.18);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #0B2238, #118184);
    color: #FFFFFF;
}

div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #D9E4EC;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 14px rgba(16, 42, 67, 0.05);
}

div[data-testid="stMetricLabel"] {
    color: #627487 !important;
}

div[data-testid="stMetricValue"] {
    color: #102A43 !important;
    font-weight: 750;
}

div[data-testid="stAlert"] {
    border-radius: 11px;
}

hr {
    border: none;
    border-top: 1px solid #D8E3EA;
    margin: 32px 0;
}

.footer {
    color: #8293A3;
    font-size: 13px;
    text-align: center;
    margin-top: 55px;
    padding-top: 20px;
    border-top: 1px solid #D8E3EA;
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.title("SynthGigCredit")

st.markdown(
    """
    <div class="subtitle">
        Evidence-driven credit assessment for gig and platform workers
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# APPLICANT INFORMATION
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="section-title">Applicant Information</div>
        <div class="small">
            Enter the applicant's financial and gig-work information.
            No document upload is required for this demo.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    applicant_id = st.text_input(
        "Applicant ID",
        value="APP-001",
        placeholder="e.g. APP-001"
    )

with col2:
    work_type = st.selectbox(
        "Employment Type",
        [
            "Gig / Platform Worker",
            "Self-employed",
            "Salaried",
            "Other"
        ]
    )

requested_amount = st.number_input(
    "Requested Credit Amount (₹)",
    min_value=0.0,
    step=500.0,
    value=10000.0
)


# =========================================================
# FINANCIAL PROFILE
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="section-title">Financial Profile</div>
        <div class="small">
            These values act as the applicant's available financial evidence.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    monthly_income = st.number_input(
        "Average Monthly Income (₹)",
        min_value=0.0,
        value=30000.0,
        step=1000.0
    )

with col2:
    monthly_expense = st.number_input(
        "Average Monthly Expenses (₹)",
        min_value=0.0,
        value=18000.0,
        step=1000.0
    )

with col3:
    monthly_debt = st.number_input(
        "Monthly Debt / EMI (₹)",
        min_value=0.0,
        value=4000.0,
        step=500.0
    )

col1, col2, col3 = st.columns(3)

with col1:
    income_volatility = st.slider(
        "Income Volatility",
        min_value=0.05,
        max_value=0.80,
        value=0.25,
        step=0.01
    )

with col2:
    platform_tenure = st.slider(
        "Platform Tenure (months)",
        min_value=1,
        max_value=24,
        value=12
    )

with col3:
    multi_platform = st.selectbox(
        "Works on Multiple Platforms",
        ["Yes", "No"]
    )


# =========================================================
# HISTORY / EVIDENCE INFORMATION
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="section-title">Evidence Quality Information</div>
        <div class="small">
            Instead of uploading documents, provide the amount of usable
            financial history and data completeness available for the applicant.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    history_length = st.selectbox(
        "Visible Financial History",
        [3, 6, 9, 12],
        index=3,
        format_func=lambda x: f"{x} months"
    )

with col2:
    aa_completeness = st.slider(
        "Account Aggregator Completeness",
        min_value=0.0,
        max_value=1.0,
        value=0.80,
        step=0.05,
        format="%.2f"
    )

with col3:
    uli_completeness = st.slider(
        "ULI Completeness",
        min_value=0.0,
        max_value=1.0,
        value=0.75,
        step=0.05,
        format="%.2f"
    )

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Applicant Age",
        min_value=18,
        max_value=70,
        value=30
    )

with col2:
    e_shram = st.selectbox(
        "e-Shram Registered",
        ["Yes", "No"]
    )


# =========================================================
# LIVE EVIDENCE CALCULATION
# =========================================================

evidence_score = (
    0.5 * (history_length / 12)
    + 0.25 * aa_completeness
    + 0.25 * uli_completeness
)

if evidence_score >= 0.60:
    evidence_status = "GOOD"
elif evidence_score >= 0.35:
    evidence_status = "PARTIAL"
else:
    evidence_status = "INSUFFICIENT"

st.markdown("---")
st.subheader("Evidence Quality")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "History",
        f"{history_length} months"
    )

with col2:
    st.metric(
        "Evidence Score",
        f"{evidence_score:.2f}"
    )

with col3:
    st.metric(
        "Evidence Status",
        evidence_status
    )


# =========================================================
# CREDIT ASSESSMENT
# =========================================================

st.markdown("---")
st.subheader("Credit Assessment")

st.caption(
    "Demo risk estimate. The current document-free UI uses a transparent "
    "heuristic until the trained XGBoost model is connected."
)

if monthly_income > 0:
    expense_ratio = monthly_expense / monthly_income
    debt_ratio = monthly_debt / monthly_income
else:
    expense_ratio = 1.0
    debt_ratio = 1.0

liquidity_ratio = (
    (monthly_income - monthly_expense - monthly_debt)
    / monthly_income
    if monthly_income > 0
    else -1
)

# Transparent demo heuristic.
pd = (
    0.05
    + 0.30 * max(0, expense_ratio - 0.50)
    + 0.20 * income_volatility
    + 0.15 * max(0, debt_ratio - 0.15)
    + 0.10 * max(0, -liquidity_ratio)
    - 0.05 * min(platform_tenure / 24, 1.0)
    - 0.03 * (1 if multi_platform == "Yes" else 0)
)

pd = float(np.clip(pd, 0.01, 0.95))

# Evidence gate
tau = 0.20

if evidence_score < tau:
    decision = "REVIEW"
    reason = "EVIDENCE_INSUFFICIENT"
elif pd < 0.20:
    decision = "APPROVE"
    reason = "PD_BELOW_THRESHOLD"
elif pd < 0.40:
    decision = "REVIEW"
    reason = "PD_MODERATE"
else:
    decision = "DECLINE"
    reason = "PD_HIGH"

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Estimated Probability of Default",
        f"{pd * 100:.1f}%"
    )

with col2:
    st.metric(
        "Expense Ratio",
        f"{expense_ratio * 100:.1f}%"
    )

with col3:
    st.metric(
        "Debt Ratio",
        f"{debt_ratio * 100:.1f}%"
    )

st.markdown("")

if decision == "APPROVE":
    st.success(f"APPROVE — {reason}")
elif decision == "REVIEW":
    st.warning(f"REVIEW — {reason}")
else:
    st.error(f"DECLINE — {reason}")


# =========================================================
# SUBMIT APPLICATION
# =========================================================

st.markdown("---")
st.subheader("Submit Application")

if st.button("Assess Applicant", use_container_width=True):

    if not applicant_id.strip():
        st.error("Please enter an Applicant ID.")

    elif monthly_income <= 0:
        st.error("Monthly income must be greater than zero.")

    else:
        applicant_folder = DATA_DIR / applicant_id.strip()
        applicant_folder.mkdir(parents=True, exist_ok=True)

        metadata_file = applicant_folder / "assessment.txt"

        metadata_file.write_text(
            f"Applicant ID: {applicant_id}\n"
            f"Employment Type: {work_type}\n"
            f"Requested Credit Amount: {requested_amount}\n"
            f"Age: {age}\n"
            f"Monthly Income: {monthly_income}\n"
            f"Monthly Expense: {monthly_expense}\n"
            f"Monthly Debt: {monthly_debt}\n"
            f"Income Volatility: {income_volatility}\n"
            f"Platform Tenure: {platform_tenure}\n"
            f"Multi Platform: {multi_platform}\n"
            f"History Length: {history_length}\n"
            f"AA Completeness: {aa_completeness}\n"
            f"ULI Completeness: {uli_completeness}\n"
            f"Evidence Score: {evidence_score:.4f}\n"
            f"Evidence Status: {evidence_status}\n"
            f"Estimated PD: {pd:.4f}\n"
            f"Decision: {decision}\n"
            f"Reason: {reason}\n"
            f"Submitted At: {datetime.now().isoformat()}\n",
            encoding="utf-8"
        )

        st.success("Application assessed successfully.")

        st.markdown(
            f"""
            <div class="card">
                <div class="section-title">Assessment Result</div>
                <div class="small">
                    Applicant <b>{applicant_id}</b> has been assessed
                    using the provided financial profile.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Probability of Default", f"{pd * 100:.1f}%")

        with col2:
            st.metric("Final Decision", decision)

        st.info(
            "No document upload was required. The applicant's financial "
            "and evidence information was entered directly into the form."
        )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        SynthGigCredit • Evidence-Quality Credit Decisioning
    </div>
    """,
    unsafe_allow_html=True
)
