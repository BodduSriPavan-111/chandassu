import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import streamlit as st
from chandassu.laghuvu_guruvu import LaghuvuGuruvu
from chandassu.padya_bhedam import check_padyam

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Telugu Chandassu",
    page_icon="📜",
    layout="wide"
)

# ------------------- Custom CSS -------------------
st.markdown("""
    <style>
        /* Remove top padding/margin */
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        
        header {
            visibility: hidden;
            height: 0;
        }
        
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        
        .result-box {
            background-color: #f7f7f7;
            padding: 1.5rem;
            border-radius: 12px;
            box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 1rem;
        }
        .column-header {
            font-size: 1.5rem;
            font-weight: bold;
            color: #2E8B57;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #2E8B57;
        }
        
        h1 {
            color: #2E8B57;
            text-align: center;
            margin-top: 0;
            padding-top: 0;
        }
        
        h2 {
            color: #555;
            text-align: center;
            font-size: 1.1rem;
            font-weight: normal;
            margin-bottom: 1.5rem;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------- Header -------------------
st.markdown("## 📜 Telugu Poetry Analyzer")
st.markdown("---")

# ------------------- Two Column Layout -------------------
col1, col2 = st.columns([1, 1])
 

# ------------------- LEFT COLUMN: INPUT -------------------
with col1:
    st.markdown('<p class="column-header">📝 Input</p>', unsafe_allow_html=True)
    
    default_text = """తొండము నేక దంతమును తోరపు బొజ్జయు వామ హస్తమున్ మెండుగ మ్రోయు గజ్జెలును మెల్లని చూపులు మందహాసమున్ కొండొక గుజ్జు రూపమున కోరిన విద్యలకెల్ల నొజ్జవై యుండెడి పార్వతీ తనయ యోయి గణాధిప నీకు మ్రొక్కెదన్"""
    
    data = st.text_area("✍️ Enter Telugu Poem", value=default_text, height=250)
    
    type_choice = st.selectbox(
        "📘 Select Chandassu Type",
        options=["vutpalamaala", "champakamaala", "saardulamu", "mattebhamu", "kandamu", "teytageethi", "aataveladi", "seesamu"]
    )
    
    analyze_button = st.button("🔍 Analyze", type="primary", use_container_width=True)

# ------------------- RIGHT COLUMN: OUTPUT -------------------
with col2:
    st.markdown('<p class="column-header">📊 Output</p>', unsafe_allow_html=True)
    
    if analyze_button:
        try:
            with st.spinner("Analyzing..."):
                # Generate Laghuvu-Guruvu sequence
                lg_data = LaghuvuGuruvu(data=data).generate()
                
                # Compute chandassu metrics
                score = check_padyam(
                    lg_data=lg_data,
                    type=type_choice,
                    return_micro_score=True,
                    verbose=False
                )
            
            st.success("✅ Analysis Complete!")
            
            # Chandassu Score
            st.markdown("#### 🌿 Chandassu Score")
            st.markdown(
                f"<div class='result-box'><h1 style='text-align:center;color:#2E8B57;margin:0;'>{score['chandassu_score']*100:.2f}%</h1></div>",
                unsafe_allow_html=True
            )

            updated_label= {"N Paadalu": "N Paadalu (N Lines)", 
                            "Gana Kramam": "Gana Kramam (Syllabic Sequence)",
                            "Yati Sthanam": "Yati Sthanam (Caesura Position)",
                            "N Aksharalu": "N Aksharalu (N Character Tokens)",
                            "Prasa": "Prasa (Alliteration)"
                           }
            # Detailed Micro Scores
            st.markdown("#### 📈 Detailed Micro Scores")
            with st.container():
                micro = score["micro_score"]
                for metric, value in micro.items():
                    st.metric(
                        label= updated_label[ metric.replace("_", " ").title() ],
                        value=f"{value*100:.2f}%"
                    )
            
            # LG Sequence
            st.markdown("#### 🔡 Laghuvu-Guruvu Sequence")
            st.code(lg_data, language="text")
            
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.info("👈 Enter text and click 'Analyze' to see results")

# ------------------- Footer -------------------
st.markdown("---")
st.markdown(
    '<p style="text-align:center;color:gray;">© 2025 Boddu Sri Pavan. Made with ❤️ for Telugu literature.</p>',
    unsafe_allow_html=True
)