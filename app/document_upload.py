import streamlit as st
from pathlib import Path
from datetime import datetime


# =========================================================
# CONFIGURATION
# =========================================================

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

st.markdown("""
<style>

.stApp {
    background-color: #F5EFE5;
    color: #302A24;
}

.block-container {
    max-width: 1100px;
    padding: 45px 55px;
}

/* Main title */

h1 {
    color: #302A24;
    font-size: 42px;
    font-weight: 700;
    letter-spacing: -1px;
}

h2, h3 {
    color: #302A24;
}

/* Subtitle */

.subtitle {
    color: #756C61;
    font-size: 17px;
    margin-top: -10px;
    margin-bottom: 35px;
}

/* Cards */

.card {
    background-color: #FBF8F2;
    border: 1px solid #DDD2C2;
    border-radius: 16px;
    padding: 25px;
    margin-bottom: 22px;
}

/* Section titles */

.section-title {
    font-size: 21px;
    font-weight: 600;
    color: #302A24;
    margin-bottom: 6px;
}

/* Small text */

.small {
    color: #756C61;
    font-size: 14px;
}

/* Upload boxes */

div[data-testid="stFileUploader"] {
    background-color: #FBF8F2;
    border: 1px dashed #B9AB98;
    border-radius: 12px;
    padding: 10px;
}

/* Buttons */

.stButton > button {
    background-color: #302A24;
    color: #F9F4EA;
    border: none;
    border-radius: 10px;
    padding: 11px 25px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #4A4036;
    color: white;
}

/* Metrics */

div[data-testid="stMetric"] {
    background-color: #F7F1E8;
    border: 1px solid #DDD2C2;
    padding: 15px;
    border-radius: 12px;
}

/* Divider */

hr {
    border-color: #DDD2C2;
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
# DOCUMENT UPLOAD
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
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ],
        help="Government-issued identity document"
    )

    bank_doc = st.file_uploader(
        "Bank Statement",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
            "csv",
            "xlsx"
        ],
        help="Recent bank statement"
    )


with col2:

    income_doc = st.file_uploader(
        "Income / Earnings Proof",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg",
            "csv",
            "xlsx"
        ],
        help="Payslip, earnings statement, or platform income record"
    )

    work_doc = st.file_uploader(
        "Employment / Platform Proof",
        type=[
            "pdf",
            "png",
            "jpg",
            "jpeg"
        ],
        help="Platform profile, contract, or employment evidence"
    )


# =========================================================
# EVIDENCE QUALITY
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
# SUBMIT APPLICANT
# =========================================================

st.markdown("---")

st.subheader("Submit Application")


if st.button(
    "Submit Applicant",
    use_container_width=True
):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    if not applicant_id.strip():

        st.error(
            "Please enter an Applicant ID."
        )

    elif uploaded_count == 0:

        st.error(
            "Please upload at least one document."
        )

    else:

        # -------------------------------------------------
        # CREATE APPLICANT DIRECTORY
        # -------------------------------------------------

        applicant_folder = (
            UPLOAD_DIR /
            applicant_id.strip()
        )

        applicant_folder.mkdir(
            parents=True,
            exist_ok=True
        )


        saved_documents = []


        # -------------------------------------------------
        # SAVE DOCUMENTS
        # -------------------------------------------------

        for name, document in documents.items():

            if document is not None:

                filename = Path(
                    document.name
                ).name

                destination = (
                    applicant_folder /
                    filename
                )

                destination.write_bytes(
                    document.getbuffer()
                )

                saved_documents.append(
                    filename
                )


        # -------------------------------------------------
        # SAVE APPLICATION METADATA
        # -------------------------------------------------

        metadata_file = (
            applicant_folder /
            "submission.txt"
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


        # -------------------------------------------------
        # SUCCESS
        # -------------------------------------------------

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
    <div
        class="small"
        style="
            margin-top:50px;
            text-align:center;
            color:#8A8074;
        "
    >
        SynthGigCredit • Evidence-Quality Credit Decisioning
    </div>
    """,
    unsafe_allow_html=True
)