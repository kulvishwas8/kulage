import streamlit as st
from datetime import date, datetime




st.set_page_config(
    page_title="Asset Allocation Calculator",
    layout="wide"
)

# Professional CSS with animations and modern design
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
              
            
        /* NEW: General rule to force inner content containers transparent */
        [data-testid="stVerticalBlock"] > div:first-child > div:first-child {
        background: transparent !important;
        }

        /* NEW: Specific targeting of the containers inside the columns */
        div[data-testid="column"] > div[data-testid="stVerticalBlock"] {
        background: transparent !important;
        }

       /* NEW: Targeting the primary content block wrappers */
        [data-testid="stVerticalBlock"] > div > div > [data-testid="stVerticalBlock"] > div:first-child > div:first-child {
        background: transparent !important;
        }
        /* ... (Keep existing Streamlit container hiding/padding rules) ... */
        .block-container {
            padding-top: 2rem !important;
            padding-bottom: 1rem !important;
            padding-left: 3rem !important;
            padding-right: 3rem !important;
            max-width: 100% !important;
        }
        
        div[data-testid="column"] > div {
            background: transparent !important;
            border: none !important;
            box-shadow: none !important;
        }
        
        [data-testid="stVerticalBlock"] {
            gap: 0 !important;
        }
        
        
        body, .stApp {
            background: linear-gradient(135deg, rgba(26, 42, 108, 0.6) 0%, rgba(42, 56, 97, 0.6) 100%) !important;
        }
        
        /* Hide default Streamlit elements */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Remove extra spacing and containers */
        .element-container {
            margin-bottom: 0 !important;
        }
        
        [data-testid="stVerticalBlock"] > [style*="flex-direction: column"] > [data-testid="stVerticalBlock"] {
            background: transparent !important;
        }
        
        section[data-testid="stSidebar"] ~ div [data-testid="column"] {
            background: transparent !important;
        }
        
        /* Header with new Deep Teal gradient and shadow */
        .main-header {
            background: linear-gradient(135deg, #007AA3 0%, #004e92 100%);
            color: white !important;
            border-radius: 20px;
            padding: 28px 24px;
            text-align: center;
            font-weight: 700;
            font-size: 2.4rem;
            margin-bottom: 28px;
            /* Update shadow to match new gradient */
            box-shadow: 0 20px 60px rgba(0, 122, 163, 0.4); 
            animation: fadeInDown 0.8s ease-out;
            position: relative;
            overflow: hidden;
        }
        
        .main-header::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255,255,255,0.1), transparent);
            animation: shine 3s infinite;
        }
        
        /* Keep all @keyframes (shine, fadeInDown, fadeInUp, scaleIn) as they are good */
        @keyframes shine {
            0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
            100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
        }
        
        @keyframes fadeInDown {
            from { opacity: 0; transform: translateY(-30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(30px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes scaleIn {
            from { opacity: 0; transform: scale(0.9); }
            to { opacity: 1; transform: scale(1); }
        }
        
        /* Card styling */
        .input-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            padding: 28px 24px;
            border-radius: 20px;
            animation: fadeInUp 0.8s ease-out;
            /* NEW: Update border color */
            border: 1px solid rgba(0, 122, 163, 0.1); 
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        
        .input-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 50px rgba(0,0,0,0.2);
        }
        
        .result-card {
            background: linear-gradient(145deg, #ffffff 0%, #f8f9fa 100%);
            box-shadow: 0 10px 40px rgba(0,0,0,0.15);
            padding: 24px 20px;
            border-radius: 20px;
            animation: scaleIn 0.8s ease-out;
            /* NEW: Update border color */
            border: 1px solid rgba(0, 122, 163, 0.1); 
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        
        .section-title {
            /* NEW: Update color to match new Teal accent */
            color: #007AA3; 
            font-size: 1.4rem;
            text-align: center;
            margin-bottom: 20px;
            font-weight: 700;
            letter-spacing: -0.5px;
        }
        
        .label-text {
            margin-bottom: 8px;
            font-weight: 700;
            /* NEW: Change to a lighter color for visibility on dark background */
            color: #1a2a6c; 
            font-size: 1.05rem;
            text-align: left;
        }
        
        .placeholder-text {
            color: #718096;
            text-align: center;
            font-size: 1.1rem;
            line-height: 1.7;
            padding: 30px 20px;
        }
        
        /* Age display - NEW: Use the new Deep Teal gradient */
        .age-display {
            background: linear-gradient(135deg, #007AA3 0%, #004e92 100%); 
            color: white;
            border-radius: 16px;
            padding: 12px;
            text-align: center;
            margin-bottom:0 auto 18px;
            width:50%
            min-width:120px
            box-shadow: 0 8px 25px rgba(0, 122, 163, 0.3); 
            animation: scaleIn 0.6s ease-out 0.2s both;
        }
        
        .age-label {
            font-size: 0.8rem;
            font-weight: 500;
            opacity: 0.95;
            margin-bottom: 3px;
        }
        
        .age-value {
            font-size: 2rem;
            font-weight: 700;
            letter-spacing: -1px;
        }
        
        /* Allocation boxes */
        .allocation-row {
            display: flex;
            gap: 12px;
            margin-bottom: 18px;
        }
        
        /* Debt Box - NEW: Blue */
        .debt-box {
            flex: 1;
            border-radius: 16px;
            background: linear-gradient(135deg, #004e92 0%, #007AA3 100%);
            color: white;
            text-align: center;
            padding: 20px 14px;
            box-shadow: 0 8px 25px rgba(0, 78, 146, 0.3);
            animation: fadeInUp 0.6s ease-out 0.3s both;
            transition: transform 0.3s ease;
        }
        
        .debt-box:hover {
            transform: scale(1.05);
        }
        
        /* Equity Box - NEW: Rich Green */
        .equity-box {
            flex: 1;
            border-radius: 16px;
            background: linear-gradient(135deg, #0a6b32 0%, #38a169 100%); 
            color: white;
            text-align: center;
            padding: 20px 14px;
            box-shadow: 0 8px 25px rgba(10, 107, 50, 0.3);
            animation: fadeInUp 0.6s ease-out 0.4s both;
            transition: transform 0.3s ease;
        }
        
        .equity-box:hover {
            transform: scale(1.05);
        }
        
        .allocation-label {
            font-size: 0.88rem;
            font-weight: 600;
            opacity: 0.95;
            margin-bottom: 7px;
            letter-spacing: 1.5px;
            text-transform: uppercase;
        }
        
        .allocation-value {
            font-size: 2.1rem;
            font-weight: 700;
            letter-spacing: -2px;
        }
        
        /* Info box */
        .info-box {
            /* Kept the light blue, as it serves well as an alert/info */
            background: linear-gradient(135deg, #e0f2fe 0%, #bae6fd 100%);
            border-left: 4px solid #0284c7;
            border-radius: 12px;
            padding: 16px;
            font-size: 0.92rem;
            color: #0c4a6e;
            line-height: 1.6;
            animation: fadeInUp 0.6s ease-out 0.5s both;
            box-shadow: 0 4px 15px rgba(2, 132, 199, 0.15);
        }
        
        /* Button styling - NEW: Use the new Deep Teal gradient */
        .stButton button {
            background: linear-gradient(135deg, #007AA3 0%, #004e92 100%) !important;
            color: white !important;
            border: none !important;
            padding: 14px 28px !important;
            font-size: 1.05rem !important;
            font-weight: 600 !important;
            border-radius: 12px !important;
            transition: all 0.3s ease !important;
            /* NEW: Update shadow to match new gradient */
            box-shadow: 0 6px 20px rgba(0, 122, 163, 0.4) !important; 
            letter-spacing: 0.5px;
        }
        
        .stButton button:hover {
            transform: translateY(-2px) !important;
            /* NEW: Update shadow to match new gradient */
            box-shadow: 0 10px 30px rgba(0, 122, 163, 0.5) !important; 
        }
        
        /* Date input styling - NEW: Update focus color */
        .stDateInput > div > div {
            background: transparent !important;
        }
        
        .stDateInput input {
            border-radius: 10px !important;
            border: 2px solid #cbd5e0 !important;
            padding: 12px 16px !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
            background: white !important;
            color: #1a202c !important;
        }
        
        .stDateInput input:focus {
            /* NEW: Update focus color */
            border-color: #007AA3 !important; 
            box-shadow: 0 0 0 3px rgba(0, 122, 163, 0.1) !important; 
        }
        
        /* ... (Keep existing Chart and Responsive rules) ... */
        .chart-wrapper {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        .stPlotlyChart {
            margin: 0 !important;
            padding: 0 !important;
        }
        
        @media (max-width: 768px) {
            .main-header {
                font-size: 1.8rem;
                padding: 20px 16px;
            }
            .allocation-value {
                font-size: 2rem;
            }
            .age-value {
                font-size: 2rem;
            }
            .block-container {
                padding-left: 1rem !important;
                padding-right: 1rem !important;
            }
        }
        /* NEW: Footer Styling for Disclaimer and Credits */
         .app-footer {
             width: 100%;
             margin-top: 30px; /* Space between last element and footer */
             padding: 15px 30px; 
             /* Dark subtle background matching the app's dark theme */
             background-color: rgba(0, 0, 0, 0.2); 
             color: #a0aec0; /* Light gray text for low contrast */
             font-size: 0.8rem;
             line-height: 1.5;
             text-align: center;
             border-top: 1px solid rgba(255, 255, 255, 0.1);
         }

         .footer-content {
             display: flex;
             flex-direction: column;
             gap: 10px;
         }

         .footer-disclaimer {
             font-weight: 400;
         }

         .footer-developer {
             font-weight: 600;
             color: #e2e8f0; /* Slightly lighter text for developer name */
         }

         /* Ensure footer spans full width on smaller screens */
         @media (min-width: 768px) {
         .footer-content {
             flex-direction: row;
             justify-content: space-between;
             align-items: center;
    }
}   
     
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header"> AgeWise Allocator</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 1.5], gap="medium")

# Processing logic (moved before columns so allocation is defined)
allocation = None
if 'last_dob' not in st.session_state:
    st.session_state.last_dob = None
    st.session_state.run = False

# Left: Input Card
with col1:
    st.markdown('''
        <div class="input-card">
            <div class="section-title">📅 Your Details</div>
            <div class="label-text">Date of Birth</div>
            <div style="height: 10px;"></div>
    ''', unsafe_allow_html=True)
    
    # Date input outside the HTML div so Streamlit can render it
    dob = st.date_input(
        "", 
        min_value=date(1900, 1, 1), 
        max_value=date.today(),
        label_visibility="collapsed",
        help="Enter your date of birth to calculate allocation",
        key="dob_input"
    )
    
    st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)
    get_it = st.button(' Get My Allocation', use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Calculate allocation
    if st.session_state.last_dob != dob:
        st.session_state.last_dob = dob
        st.session_state.run = False

    if get_it or st.session_state.run:
        st.session_state.run = True
        dob_datetime = datetime.combine(dob, datetime.min.time())
        today_datetime = datetime.now()
        age_days = (today_datetime - dob_datetime).days
        age_years = age_days / 365.25
        max_age = 85
        debt_pct = min((age_years / max_age) * 100, 100)
        equity_pct = 100 - debt_pct
        if equity_pct < 10:
            equity_pct = 10
            debt_pct = 90
        allocation = {
            "debt": round(debt_pct, 2),
            "equity": round(equity_pct, 2),
            "age": int(age_years)
        }
    
    
    # NEW: Investment Strategy Info Box (Moved from col2)
    if allocation:
        st.markdown('<div style="height: 20px;"></div>', unsafe_allow_html=True)
        st.markdown('<div class="input-card" style="padding: 20px;">', unsafe_allow_html=True)
        st.markdown(
            '<div class="info-box">'
            '💡 <strong>Secure your future with a strategy that evolves as you do.' \
            'Retire confidently knowing your portfolio automatically balances growth (Equity) and safety (Debt) over time.'
            '</div>',
            unsafe_allow_html=True
        )
        st.markdown('</div>', unsafe_allow_html=True)
    

# Right: Result Card
with col2:
    if allocation:
        st.markdown('<div class="result-card">', unsafe_allow_html=True)

         # Allocation Boxes
        st.markdown(
            f'<div class="allocation-row">'
            f'<div class="debt-box">'
            f'<div class="allocation-label">💰 Debt</div>'
            f'<div class="allocation-value">{allocation["debt"]}%</div>'
            f'</div>'
            f'<div class="equity-box">'
            f'<div class="allocation-label">📈 Equity</div>'
            f'<div class="allocation-value">{allocation["equity"]}%</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        # Age Display
        st.markdown(
            f'<div class="age-display">'
            f'<div class="age-label">Your Age</div>'
            f'<div class="age-value">{allocation["age"]}</div>'
            f'<div class="age-label">years old</div>'
            f'</div>',
            unsafe_allow_html=True
        )

        st.markdown("""
            <div class="app-footer">
                <div class="footer-content">
                   <div class="footer-disclaimer">
                        Disclaimer: This AgeWise Allocator tool is provided for informational and educational purposes only.
                   </div>
                   <div class="footer-developer">
                       Developed by: Vishwas Kulkarni (vishwaskulkarni@Zohomail.in)
                   </div>
                </div>
            </div>
""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True) 
        

    else:
        st.markdown(
            '<div class="result-card">'
            '<div class="placeholder-text">'
            '👈 Enter your Date of Birth and click Get My Allocation to instantly see your personalized portfolio split.'
            '</div>'
            '</div>',
            unsafe_allow_html=True

        )
