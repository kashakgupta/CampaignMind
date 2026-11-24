import streamlit as st
import pandas as pd
import joblib
import json
import os
# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="CampaignMind",
    page_icon="assets/campaignmind_logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# PROJECT PATHS
# ==========================================

PROJECT_PATH = "/content/drive/MyDrive/Marketing-Campaign-Prediction"
MODEL_PATH = os.path.join(PROJECT_PATH, "models")
RESULTS_PATH = os.path.join(PROJECT_PATH, "results")
GRAPHS_PATH = os.path.join(RESULTS_PATH, "graphs")

# ==========================================
# LOAD MODEL, PREPROCESSOR AND RESULTS
# ==========================================

@st.cache_resource
def load_model():
    model = joblib.load(
        os.path.join(MODEL_PATH, "random_forest_model.pkl")
    )
    preprocessor = joblib.load(
        os.path.join(MODEL_PATH, "preprocessor.pkl")
    )
    return model, preprocessor


@st.cache_data
def load_json(filename):
    path = os.path.join(RESULTS_PATH, filename)
    with open(path, "r") as file:
        return json.load(file)


model, preprocessor = load_model()
rf_results = load_json("random_forest_results.json")
ann_results = load_json("ann_results.json")
comparison = load_json("model_comparison.json")

# ==========================================
# CAMPAIGNMIND LOGO — C MONOGRAM
# ==========================================
logo_svg = """
<svg class="brand-icon" viewBox="0 0 100 100"
     xmlns="http://www.w3.org/2000/svg"
     role="img" aria-label="CampaignMind logo">
    <path d="M76 25 A34 34 0 1 0 77 76"
          fill="none" stroke="#A9D6E5"
          stroke-width="9" stroke-linecap="round"/>
    <path d="M40 67 L57 48 L68 54 L86 30"
          fill="none" stroke="#A9D6E5"
          stroke-width="6" stroke-linecap="round"
          stroke-linejoin="round"/>
    <path d="M72 30 H86 V44"
          fill="none" stroke="#A9D6E5"
          stroke-width="6" stroke-linecap="round"
          stroke-linejoin="round"/>
</svg>
"""

# ==========================================
# CAMPAIGNMIND THEME — CREAM, BROWN & BABY BLUE
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.cdnfonts.com/css/ragellan');

:root {
    --cm-cream: #F5EBDD;
    --cm-ivory: #FFF9F0;
    --cm-brown: #4A3428;
    --cm-brown-soft: #806653;
    --cm-border: #D8C6B2;
    --cm-blue: #A9D6E5;
    --cm-blue-hover: #A9D6E5;
    --cm-blue-text: #28566B;
}

/* Global layout and typography */
html, body, [class*="css"] {
    font-family: 'Ragellan', serif !important;
}

.stApp {
    background: var(--cm-cream) !important;
    color: var(--cm-brown) !important;
}

.block-container {
    padding-top: 2.5rem;
    padding-bottom: 2rem;
    color: var(--cm-brown) !important;
}

[data-testid="stHeader"] {
    background: transparent !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #EDE0CE !important;
}

section[data-testid="stSidebar"] p,
section[data-testid="stSidebar"] label,
section[data-testid="stSidebar"] span {
    color: var(--cm-brown) !important;
}

section[data-testid="stSidebar"] hr {
    border-color: var(--cm-border) !important;
}

/* Branding */
.brand-logo {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 8px 0 10px 0;
}

.brand-icon {
    width: 52px;
    height: 52px;
    flex-shrink: 0;
}

.brand-name {
    font-size: 25px;
    font-weight: 800;
    letter-spacing: -1px;
    color: var(--cm-brown) !important;
    white-space: nowrap;
}

.brand-name span,
.main-brand .brand-name span {
    color: var(--cm-blue) !important;
}

.brand-tagline {
    color: var(--cm-brown-soft) !important;
    font-size: 11px;
    letter-spacing: 2px;
    margin-top: 3px;
}

.main-brand {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 5px;
}

.main-brand .brand-icon {
    width: 66px;
    height: 66px;
}

.main-brand .brand-name {
    color: var(--cm-brown) !important;
    font-size: 42px;
}

.page-subtitle {
    color: var(--cm-brown-soft) !important;
    font-size: 15px;
    margin: 5px 0 28px 0;
}

/* Headings and body copy */
.section-heading {
    color: var(--cm-brown) !important;
    font-size: 22px;
    font-weight: 800;
    margin: 22px 0 12px 0;
}

.stMarkdown h1,
.stMarkdown h2,
.stMarkdown h3,
.stMarkdown h4 {
    color: var(--cm-brown) !important;
}

.stMarkdown p,
.stMarkdown li,
.stCaption,
[data-testid="stCaptionContainer"] {
    color: var(--cm-brown-soft) !important;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: var(--cm-ivory) !important;
    border: 1px solid var(--cm-border) !important;
    border-top: 4px solid var(--cm-blue) !important;
    border-radius: 14px !important;
    padding: 20px 18px !important;
    min-height: 112px;
    box-shadow: 0 4px 14px rgba(74, 52, 40, 0.07) !important;
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] p {
    color: var(--cm-brown-soft) !important;
    font-size: 14px !important;
    font-weight: 700 !important;
}

div[data-testid="stMetricValue"],
div[data-testid="stMetricValue"] div {
    color: var(--cm-brown) !important;
    font-size: 27px !important;
    font-weight: 800 !important;
}

/* All Streamlit buttons: same baby-blue colour, including active navigation */
.stButton > button,
.stButton > button[kind="primary"],
.stButton > button[kind="secondary"],
button[data-testid="stBaseButton-primary"],
button[data-testid="stBaseButton-secondary"],
div[data-testid="stFormSubmitButton"] button,
div[data-testid="stForm"] button[kind="primary"] {
    background: var(--cm-blue) !important;
    background-color: var(--cm-blue) !important;
    background-image: none !important;
    color: var(--cm-blue-text) !important;
    -webkit-text-fill-color: var(--cm-blue-text) !important;
    border: 1px solid #80BBD0 !important;
    border-radius: 10px !important;
    min-height: 42px !important;
    font-weight: 750 !important;
    opacity: 1 !important;
    box-shadow: none !important;
    transition: none !important;
}

.stButton > button *,
button[data-testid="stBaseButton-primary"] *,
button[data-testid="stBaseButton-secondary"] *,
div[data-testid="stFormSubmitButton"] button *,
div[data-testid="stForm"] button[kind="primary"] * {
    color: var(--cm-blue-text) !important;
    -webkit-text-fill-color: var(--cm-blue-text) !important;
}

.stButton > button:hover,
button[data-testid="stBaseButton-primary"]:hover,
button[data-testid="stBaseButton-secondary"]:hover,
div[data-testid="stFormSubmitButton"] button:hover,
div[data-testid="stForm"] button[kind="primary"]:hover {
    background: var(--cm-blue) !important;
    background-color: var(--cm-blue) !important;
    background-image: none !important;
    color: var(--cm-blue-text) !important;
    border-color: #80BBD0 !important;
}

.stButton > button:focus,
.stButton > button:focus-visible,
button[data-testid="stBaseButton-primary"]:focus-visible {
    outline: 2px solid var(--cm-blue-text) !important;
    outline-offset: 2px !important;
}

.stButton > button:disabled,
div[data-testid="stFormSubmitButton"] button:disabled {
    background: var(--cm-blue) !important;
    color: var(--cm-blue-text) !important;
    opacity: 0.75 !important;
}

/* Dropdowns and form controls */
.stSelectbox label,
.stNumberInput label,
.stTextInput label,
.stRadio label,
.stMultiSelect label,
.stDateInput label {
    color: var(--cm-brown) !important;
    font-weight: 700 !important;
}

div[data-baseweb="select"] > div {
    background: var(--cm-ivory) !important;
    border: 1px solid var(--cm-border) !important;
    color: var(--cm-brown) !important;
}

div[data-baseweb="select"] input,
div[data-baseweb="select"] span {
    color: var(--cm-brown) !important;
}

div[data-baseweb="popover"],
div[data-baseweb="menu"],
ul[role="listbox"] {
    background: var(--cm-ivory) !important;
}

li[role="option"] {
    background: var(--cm-ivory) !important;
    color: var(--cm-brown) !important;
}

li[role="option"]:hover {
    background: var(--cm-blue) !important;
    color: var(--cm-blue-text) !important;
}

.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stTextArea textarea {
    background: var(--cm-ivory) !important;
    color: var(--cm-brown) !important;
    border: 1px solid var(--cm-border) !important;
}

/* Tabs and dividers */
button[data-baseweb="tab"] {
    color: var(--cm-brown-soft) !important;
    font-weight: 650;
}

button[data-baseweb="tab"][aria-selected="true"] {
    color: var(--cm-blue-text) !important;
    border-bottom-color: var(--cm-blue) !important;
}

hr {
    border-color: var(--cm-border) !important;
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# CAMPAIGNMIND DEMO AUTHENTICATION
# ==========================================

DEMO_EMAIL = "kashak17@gmail.com"
DEMO_PASSWORD = "Kashak17@123"

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:

    st.markdown("""
        <div style="text-align:center; padding:55px 0 20px 0;">
            <h1 style="color:#4A3428; font-size:42px;">
                Campaign<span style="color:#A9D6E5;">Mind</span>
            </h1>
            <p style="color:#806653; letter-spacing:2px;">
                CAMPAIGN INTELLIGENCE
            </p>
            
        </div>
    """, unsafe_allow_html=True)

    left, center, right = st.columns([1, 1.2, 1])

    with center:
        with st.form("campaignmind_login_form"):

            st.subheader("Sign In")

            email = st.text_input(
                "Email Address",
                placeholder="Enter your email"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            login_button = st.form_submit_button(
                "Sign In",
                use_container_width=True,
                type="primary"
            )

            if login_button:
                if email == DEMO_EMAIL and password == DEMO_PASSWORD:
                    st.session_state.authenticated = True
                    st.rerun()
                else:
                    st.error("Invalid email or password. Please try again.")

    st.stop()

# ==========================================
# END DEMO AUTHENTICATION
# ==========================================

# ==========================================
# SIDEBAR AND NAVIGATION
# ==========================================

with st.sidebar:

    # CampaignMind branding
    st.html(f"""
    <div style="padding:12px 4px 18px 4px;">
        <div class="brand-logo">
            {logo_svg}
            <div class="brand-name">
                Campaign<span>Mind</span>
            </div>
        </div>
        <div class="brand-tagline">
            CAMPAIGN INTELLIGENCE
        </div>
    </div>
""")

    st.divider()

    # Navigation heading
    st.markdown(
        """
        <p style="
            color:#806653;
            font-size:13px;
            font-weight:700;
            letter-spacing:1px;
        ">NAVIGATION</p>
        """,
        unsafe_allow_html=True
    )

    # Navigation options
    navigation_pages = [
        "Dashboard",
        "Predict Subscription",
        "EDA Insights",
        "Model Comparison"
    ]

    if "selected_page" not in st.session_state:
        st.session_state.selected_page = "Dashboard"

    for page_name in navigation_pages:

        if st.button(
            page_name,
            key="nav_" + page_name.replace(" ", "_").lower(),
            type=(
                "primary"
                if st.session_state.selected_page == page_name
                else "secondary"
            ),
            use_container_width=True
        ):
            st.session_state.selected_page = page_name
            st.rerun()

    page = st.session_state.selected_page


# ==========================================
# MAIN HEADER
# ==========================================

st.html(f"""
    <div class="main-brand">
        {logo_svg}
        <div class="brand-name">
            Campaign<span>Mind</span>
        </div>
    </div>

    <div class="page-subtitle">
        Explore customer trends, compare predictive models, and predict
        customer subscription likelihood.
    </div>
""")

# ==========================================
# DASHBOARD PAGE
# ==========================================

if page == "Dashboard":

    st.markdown(
        '<div class="section-heading">Campaign Overview</div>',
        unsafe_allow_html=True
    )

    selected_model = st.selectbox(
        "Select model to explore",
        ["Random Forest", "Artificial Neural Network"],
        key="dashboard_model_selector"
    )

    selected_results = (
        rf_results if selected_model == "Random Forest" else ann_results
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Records", "45,211")
    with col2:
        st.metric("Input Features", "15")
    with col3:
        st.metric("Models Evaluated", "2")
    with col4:
        st.metric("Selected Model", selected_model)

    st.markdown(
        f'<div class="section-heading">{selected_model} – Performance</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Accuracy", f"{selected_results['accuracy'] * 100:.2f}%")
    with col2:
        st.metric("Precision", f"{selected_results['precision'] * 100:.2f}%")
    with col3:
        st.metric("Recall", f"{selected_results['recall'] * 100:.2f}%")
    with col4:
        st.metric("F1 Score", f"{selected_results['f1_score'] * 100:.2f}%")

# ==========================================
# PREDICTION PAGE
# ==========================================

elif page == "Predict Subscription":

    st.markdown("## Customer Subscription Prediction")
    st.write(
        "Enter the customer's details below to estimate "
        "their likelihood of subscribing to a term deposit."
    )
    st.markdown("---")

    with st.form("customer_prediction_form"):

        st.markdown("### Personal Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            age = st.number_input(
                "Age", min_value=18, max_value=100, value=35
            )
        with col2:
            job = st.selectbox(
                "Job",
                [
                    "admin.", "blue-collar", "entrepreneur", "housemaid",
                    "management", "retired", "self-employed", "services",
                    "student", "technician", "unemployed", "unknown"
                ]
            )
        with col3:
            marital = st.selectbox(
                "Marital Status", ["married", "single", "divorced"]
            )

        col1, col2 = st.columns(2)
        with col1:
            education = st.selectbox(
                "Education", ["primary", "secondary", "tertiary", "unknown"]
            )
        with col2:
            default = st.selectbox("Has Credit in Default?", ["no", "yes"])

        st.markdown("---")
        st.markdown("### Financial Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            balance = st.number_input(
                "Average Yearly Balance (€)",
                min_value=-100000, max_value=1000000, value=1000
            )
        with col2:
            housing = st.selectbox("Housing Loan?", ["no", "yes"])
        with col3:
            loan = st.selectbox("Personal Loan?", ["no", "yes"])

        st.markdown("---")
        st.markdown("### Campaign Information")
        col1, col2, col3 = st.columns(3)

        with col1:
            contact = st.selectbox(
                "Contact Communication Type",
                ["cellular", "telephone", "unknown"]
            )
        with col2:
            day = st.number_input(
                "Last Contact Day", min_value=1, max_value=31, value=15
            )
        with col3:
            month = st.selectbox(
                "Last Contact Month",
                [
                    "jan", "feb", "mar", "apr", "may", "jun",
                    "jul", "aug", "sep", "oct", "nov", "dec"
                ]
            )

        col1, col2, col3 = st.columns(3)
        with col1:
            campaign = st.number_input(
                "Contacts During This Campaign",
                min_value=1, max_value=100, value=2
            )
        with col2:
            pdays = st.number_input(
                "Days Since Previous Contact (-1 if never contacted)",
                min_value=-1, max_value=999, value=-1
            )
        with col3:
            previous = st.number_input(
                "Contacts Before This Campaign",
                min_value=0, max_value=100, value=0
            )

        poutcome = st.selectbox(
            "Previous Campaign Outcome",
            ["unknown", "failure", "other", "success"]
        )

        submitted = st.form_submit_button(
            "Predict Subscription",
            use_container_width=True
        )

    if submitted:
        customer_data = pd.DataFrame([{
            "age": age,
            "job": job,
            "marital": marital,
            "education": education,
            "default": default,
            "balance": balance,
            "housing": housing,
            "loan": loan,
            "contact": contact,
            "day": day,
            "month": month,
            "campaign": campaign,
            "pdays": pdays,
            "previous": previous,
            "poutcome": poutcome
        }])

        try:
            transformed_data = preprocessor.transform(customer_data)
            prediction = model.predict(transformed_data)[0]
            probabilities = model.predict_proba(transformed_data)[0]
            subscription_probability = float(probabilities[1])

            st.markdown("---")
            st.markdown("### Prediction Result")

            if prediction == 1:
                st.success("Likely to Subscribe")
            else:
                st.warning("Unlikely to Subscribe")

            st.metric(
                "Subscription Probability",
                f"{subscription_probability * 100:.2f}%"
            )
            st.progress(subscription_probability)
            st.caption(
                "Probability is the Random Forest model's estimate, "
                "not a guarantee of customer behaviour."
            )

        except Exception as e:
            st.error(f"Prediction failed: {e}")

# ==========================================
# EDA INSIGHTS PAGE
# ==========================================

elif page == "EDA Insights":

    st.markdown("## Exploratory Data Analysis")
    st.write(
        "Explore customer demographics, campaign patterns "
        "and relationships in the Bank Marketing dataset."
    )

    def show_graph(title, filename, description):
        graph_path = os.path.join(GRAPHS_PATH, filename)
        st.markdown(f"### {title}")
        st.caption(description)

        if os.path.exists(graph_path):
            st.image(graph_path, use_container_width=True)
        else:
            st.warning(f"Graph not found: {filename}")

    st.markdown("---")
    st.markdown("### 1. Customer Distribution")

    col1, col2 = st.columns(2)
    with col1:
        show_graph(
            "Age Distribution",
            "age_distribution.png",
            "Distribution of customers across different age groups."
        )
    with col2:
        show_graph(
            "Job Distribution",
            "job_distribution.png",
            "Distribution of customers across occupational categories."
        )

    col1, col2 = st.columns(2)
    with col1:
        show_graph(
            "Subscription Distribution",
            "target_distribution.png",
            "Distribution of customers who subscribed and did not subscribe."
        )
    with col2:
        show_graph(
            "Correlation Heatmap",
            "correlation_heatmap.png",
            "Relationships between numerical variables in the dataset."
        )

    st.markdown("---")
    st.markdown("### 2. Campaign Insights")

    campaign_graphs = [
        (
            "Subscription by Contact Type",
            "subscription_by_contact.png",
            "Subscription outcomes across communication channels."
        ),
        (
            "Subscription by Education",
            "subscription_by_education.png",
            "Subscription patterns across education levels."
        ),
        (
            "Subscription by Housing Loan",
            "subscription_by_housing.png",
            "Relationship between housing loans and subscription outcomes."
        ),
        (
            "Subscription by Job",
            "subscription_by_job.png",
            "Subscription outcomes across occupational categories."
        ),
        (
            "Subscription by Marital Status",
            "subscription_by_marital.png",
            "Subscription patterns across marital status categories."
        ),
        (
            "Subscription by Month",
            "subscription_by_month.png",
            "Variation in subscription outcomes across campaign months."
        ),
        (
            "Subscription by Previous Outcome",
            "subscription_by_poutcome.png",
            "Subscription patterns based on previous campaign outcomes."
        )
    ]

    for i in range(0, len(campaign_graphs), 2):
        col1, col2 = st.columns(2)

        with col1:
            title, filename, description = campaign_graphs[i]
            show_graph(title, filename, description)

        if i + 1 < len(campaign_graphs):
            with col2:
                title, filename, description = campaign_graphs[i + 1]
                show_graph(title, filename, description)

# ==========================================
# MODEL COMPARISON PAGE
# ==========================================

elif page == "Model Comparison":

    st.markdown("## Model Performance Comparison")
    st.markdown(
        "Evaluate Random Forest and Artificial Neural Network "
        "using the project's saved evaluation results."
    )

    st.markdown("### Performance Metrics")
    col1, col2 = st.columns(2)

    metric_keys = [
        ("accuracy", "Accuracy"),
        ("precision", "Precision"),
        ("recall", "Recall"),
        ("f1_score", "F1 Score"),
        ("roc_auc", "ROC-AUC")
    ]

    with col1:
        st.markdown("#### Random Forest")
        for key, label in metric_keys:
            value = rf_results.get(key)
            if value is not None:
                st.metric(label, f"{value:.4f}")

    with col2:
        st.markdown("#### Artificial Neural Network")
        for key, label in metric_keys:
            value = ann_results.get(key)
            if value is not None:
                st.metric(label, f"{value:.4f}")

    st.divider()
    st.markdown("### Direct Model Comparison")

    comparison_graphs = [
        ("Overall Performance", "model_performance_comparison.png"),
        ("Precision, Recall and F1 Score", "precision_recall_f1_comparison.png"),
        ("ROC-AUC Comparison", "roc_auc_comparison.png"),
        ("Confusion Matrix Comparison", "model_confusion_matrix_comparison.png")
    ]

    for title, filename in comparison_graphs:
        st.markdown(f"#### {title}")
        graph_path = os.path.join(GRAPHS_PATH, filename)

        if os.path.exists(graph_path):
            st.image(graph_path, use_container_width=True)
        else:
            st.warning(f"Graph not found: {filename}")

    st.divider()
    st.markdown("### Explore Individual Model Insights")
    st.markdown(
        "Select a machine learning model to explore its evaluation results."
    )

    selected_model = st.selectbox(
        "Choose Model",
        ["Random Forest", "Artificial Neural Network"],
        key="insights_model_selector"
    )

    if selected_model == "Random Forest":
        st.markdown("#### Random Forest Analysis")
        model_graphs = [
            ("Confusion Matrix", "rf_confusion_matrix.png"),
            ("ROC Curve", "rf_roc_curve.png"),
            ("Feature Importance", "rf_feature_importance.png")
        ]
    else:
        st.markdown("#### Artificial Neural Network Analysis")
        model_graphs = [
            ("Confusion Matrix", "ann_confusion_matrix.png"),
            ("ROC Curve", "ann_roc_curve.png"),
            ("Training and Validation Accuracy",
             "ann_training_validation_accuracy.png"),
            ("Training and Validation Loss",
             "ann_training_validation_loss.png")
        ]

    for title, filename in model_graphs:
        st.markdown(f"#### {title}")
        graph_path = os.path.join(GRAPHS_PATH, filename)

        if os.path.exists(graph_path):
            st.image(graph_path, use_container_width=True)
        else:
            st.warning(f"Graph not found: {filename}")

    st.divider()
    st.markdown("### Final Model Selection")
    st.markdown(
        "**Random Forest** is selected as the final prediction model "
        "because it achieved the strongest overall balance across accuracy, "
        "precision, F1 score and ROC-AUC. ANN achieved higher recall, "
        "but its overall F1 score was slightly lower."
    )

    st.caption(
        "Metrics shown above are baseline evaluation results. "
        "The separately tuned ANN threshold is not mixed into this comparison."
    )
