import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(
    page_title="SynthGigCredit",
    page_icon="◐",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parents[1]
UPLOAD_DIR = BASE_DIR / "data" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

# =========================================================
# CUSTOM STYLING
# =========================================================

st.markdown(
    """
    <style>

    /* ---------- Main page ---------- */

    .stApp {
        background:
            linear-gradient(
                135deg,
                #F4F8FB 0%,
                #EEF5F7 50%,
                #F8FAFC 100%
            );
        color: #172033;
    }

    .block-container {
        max-width: 1150px;
        padding: 45px 55px 60px 55px;
    }

    /* ---------- Header ---------- */

    h1 {
        color: #102A43 !important;
        font-size: 46px !important;
        font-weight: 750 !important;
        letter-spacing: -1.5px;
        margin-bottom: 5px;
    }

    h2, h3 {
        color: #102A43 !important;
    }

    .subtitle {
        color: #526477;
        font-size: 18px;
        margin-bottom: 35px;
    }

    /* ---------- Cards ---------- */

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

    /* ---------- Input fields ---------- */

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

    /* ---------- File uploader ---------- */

    div[data-testid="stFileUploader"] {
        background: #F8FBFD;
        border: 1.5px dashed #9BB7C9;
        border-radius: 14px;
        padding: 12px;
        transition: 0.2s;
    }

    div[data-testid="stFileUploader"]:hover {
        border-color: #159A9C;
        background: #F2FAFA;
    }

    /* ---------- Buttons ---------- */

    .stButton > button {
        background: linear-gradient(
            135deg,
            #102A43,
            #159A9C
        );
        color: #FFFFFF;
        border: none;
        border-radius: 11px;
        padding: 13px 26px;
        font-size: 16px;
        font-weight: 700;
        box-shadow: 0 5px 14px rgba(16, 42, 67, 0.18);
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(
            135deg,
            #0B2238,
            #118184
        );
        color: #FFFFFF;
        transform: translateY(-1px);
        box-shadow: 0 7px 18px rgba(16, 42, 67, 0.24);
    }

    /* ---------- Metrics ---------- */

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

    /* ---------- Success / warning messages ---------- */

    div[data-testid="stAlert"] {
        border-radius: 11px;
    }

    /* ---------- Divider ---------- */

    hr {
        border: none;
        border-top: 1px solid #D8E3EA;
        margin: 32px 0;
    }

    /* ---------- Footer ---------- */

    .footer {
        color: #8293A3;
        font-size: 13px;
        text-align: center;
        margin-top: 55px;
        padding-top: 20px;
        border-top: 1px solid #D8E3EA;
    }

    </style>
    """,
    unsafe_allow_html=True
)

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
        <div class="section-title">
            Applicant Information
        </div>
        <div class="small">
            Enter the basic information required for the credit assessment.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    applicant_id = st.text_input(
        "Applicant ID",
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
    "Requested Credit Amount",
    min_value=0.0,
    step=500.0,
    value=10000.0
)

# =========================================================
# APPLICANT EVIDENCE
# =========================================================

st.markdown(
    """
    <div class="card">
        <div class="section-title">
            Applicant Evidence
        </div>
        <div class="small">
            Upload the documents available for this applicant.
            Evidence quality will be considered before a final decision.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:

    identity_doc = st.file_uploader(
        "Identity Proof",
        type=["pdf", "png", "jpg", "jpeg"],
        help="Government-issued identity document"
    )

    bank_doc = st.file_uploader(
        "Bank Statement",
        type=["pdf", "png", "jpg", "jpeg", "csv", "xlsx"],
        help="Recent bank statement"
    )

with col2:

    income_doc = st.file_uploader(
        "Income / Earnings Proof",
        type=["pdf", "png", "jpg", "jpeg", "csv", "xlsx"],
        help="Payslip, earnings statement, or platform income record"
    )

    work_doc = st.file_uploader(
        "Employment / Platform Proof",
        type=["pdf", "png", "jpg", "jpeg"],
        help="Platform profile, contract, or employment evidence"
    )

# =========================================================
# DOCUMENT INFORMATION
# =========================================================

documents = {
    "Identity": identity_doc,
    "Bank statement": bank_doc,
    "Income / earnings": income_doc,
    "Employment / platform": work_doc
}

uploaded_count = sum(
    1
    for document in documents.values()
    if document is not None
)

# =========================================================
# EVIDENCE QUALITY
# =========================================================

st.markdown("---")

st.subheader("Evidence Quality")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Documents Provided",
        f"{uploaded_count}/4"
    )

with col2:

    completeness = int(
        (uploaded_count / 4) * 100
    )

    st.metric(
        "Completeness",
        f"{completeness}%"
    )

with col3:

    if uploaded_count >= 3:
        evidence_status = "GOOD"

    elif uploaded_count >= 1:
        evidence_status = "PARTIAL"

    else:
        evidence_status = "INSUFFICIENT"

    st.metric(
        "Evidence Status",
        evidence_status
    )

# =========================================================
# DOCUMENT STATUS
# =========================================================

st.markdown("")

for name, document in documents.items():

    if document is not None:

        st.success(
            f"✓ {name} provided"
        )

    else:

        st.warning(
            f"○ {name} not provided"
        )

# =========================================================
# SUBMIT APPLICATION
# =========================================================

st.markdown("---")

st.subheader("Submit Application")

if st.button(
    "Submit Applicant",
    use_container_width=True
):

    if not applicant_id.strip():

        st.error(
            "Please enter an Applicant ID."
        )

    elif uploaded_count == 0:

        st.error(
            "Please upload at least one document."
        )

    else:

        applicant_folder = (
            UPLOAD_DIR / applicant_id.strip()
        )

        applicant_folder.mkdir(
            parents=True,
            exist_ok=True
        )

        saved_documents = []

        # Save uploaded documents
        for name, document in documents.items():

            if document is not None:

                filename = Path(
                    document.name
                ).name

                destination = (
                    applicant_folder / filename
                )

                destination.write_bytes(
                    document.getbuffer()
                )

                saved_documents.append(
                    filename
                )

        # Save metadata
        metadata_file = (
            applicant_folder / "submission.txt"
        )

        metadata_file.write_text(
            f"Applicant ID: {applicant_id}\n"
            f"Employment Type: {work_type}\n"
            f"Requested Credit Amount: {requested_amount}\n"
            f"Documents Provided: {uploaded_count}/4\n"
            f"Evidence Completeness: {completeness}%\n"
            f"Evidence Status: {evidence_status}\n"
            f"Submitted At: {datetime.now().isoformat()}\n"
            f"Documents: {', '.join(saved_documents)}\n",
            encoding="utf-8"
        )

        # Success
        st.success(
            "Application submitted successfully."
        )

        st.info(
            f"{uploaded_count} document(s) saved for "
            f"{applicant_id}."
        )

        st.markdown(
            """
            <div class="card">
                <div class="section-title">
                    Application Received
                </div>

                <div class="small">
                    The submitted evidence can now be passed
                    through the evidence-quality, policy, and
                    credit decision pipeline.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #F4F7FB;
        color: #172033;
    }

    .block-container {
        max-width: 1150px;
        padding: 45px 55px 60px 55px;
    }

    h1 {
        color: #0F2742 !important;
        font-size: 46px !important;
        font-weight: 750 !important;
        letter-spacing: -1.5px;
    }

    h2, h3 {
        color: #0F2742 !important;
    }

    .subtitle {
        color: #60758A;
        font-size: 18px;
        margin-bottom: 35px;
    }

    .card {
        background-color: #FFFFFF;
        border: 1px solid #D8E1EA;
        border-radius: 16px;
        padding: 26px 28px;
        margin-bottom: 22px;
        box-shadow: 0 4px 15px rgba(15, 39, 66, 0.06);
    }

    .section-title {
        color: #0F2742;
        font-size: 22px;
        font-weight: 700;
        margin-bottom: 7px;
    }

    .small {
        color: #60758A;
        font-size: 14px;
        line-height: 1.6;
    }

    label {
        color: #263B53 !important;
        font-weight: 600 !important;
    }

    div[data-baseweb="input"] {
        background-color: #FFFFFF;
        border: 1px solid #C8D4DF;
        border-radius: 10px;
    }

    div[data-baseweb="input"]:focus-within {
        border-color: #2878C8;
        box-shadow: 0 0 0 2px rgba(40, 120, 200, 0.12);
    }

    div[data-baseweb="select"] > div {
        background-color: #FFFFFF;
        border: 1px solid #C8D4DF;
        border-radius: 10px;
    }

    div[data-testid="stFileUploader"] {
        background-color: #FFFFFF;
        border: 1.5px dashed #9FB4C8;
        border-radius: 14px;
        padding: 12px;
    }

    div[data-testid="stFileUploader"]:hover {
        border-color: #2878C8;
        background-color: #F7FAFD;
    }

    .stButton > button {
        background-color: #0F2742;
        color: #FFFFFF;
        border: none;
        border-radius: 10px;
        padding: 13px 26px;
        font-size: 16px;
        font-weight: 700;
    }

    .stButton > button:hover {
        background-color: #17466F;
        color: #FFFFFF;
    }

    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #D8E1EA;
        padding: 18px;
        border-radius: 14px;
        box-shadow: 0 3px 12px rgba(15, 39, 66, 0.05);
    }

    div[data-testid="stMetricLabel"] {
        color: #60758A !important;
    }

    div[data-testid="stMetricValue"] {
        color: #0F2742 !important;
        font-weight: 750;
    }

    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    hr {
        border: none;
        border-top: 1px solid #D8E1EA;
        margin: 32px 0;
    }

    .footer {
        color: #8192A3;
        font-size: 13px;
        text-align: center;
        margin-top: 55px;
        padding-top: 20px;
        border-top: 1px solid #D8E1EA;
    }

    </style>
    """,
    unsafe_allow_html=True
)