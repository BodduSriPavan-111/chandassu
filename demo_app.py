import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '..')))

import streamlit as st
import pandas as pd
from chandassu.telugu.padya_bhedam import find_padyam

# ------------------- Page Config -------------------
st.set_page_config(
    page_title="Telugu Chandassu - Detect Type",
    page_icon="🔍",
    layout="wide"
)

# ------------------- Custom CSS -------------------
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem !important;
            padding-bottom: 0rem !important;
        }
        header { visibility: hidden; height: 0; }
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
        h1 { color: #2E8B57; text-align: center; margin-top: 0; padding-top: 0; }
        h2 { color: #555; text-align: center; font-size: 1.1rem; font-weight: normal; margin-bottom: 1.5rem; }
    </style>
""", unsafe_allow_html=True)

# ------------------- Header -------------------
st.markdown("## 🔍 Telugu Padyam Type Detector")
st.markdown("---")

# ------------------- Two Column Layout -------------------
col1, col2 = st.columns([1, 1])

# ------------------- LEFT COLUMN: INPUT -------------------
with col1:
    st.markdown('<p class="column-header">📝 Input</p>', unsafe_allow_html=True)

    default_text = """తొండము నేక దంతమును తోరపు బొజ్జయు వామ హస్తమున్ మెండుగ మ్రోయు గజ్జెలును మెల్లని చూపులు మందహాసమున్ కొండొక గుజ్జు రూపమున కోరిన విద్యలకెల్ల నొజ్జవై యుండెడి పార్వతీ తనయ యోయి గణాధిప నీకు మ్రొక్కెదన్"""

    padyam = st.text_area("✍️ Enter Telugu Poem", value=default_text, height=250)

    analyze_button = st.button("🔍 Analyze", type="primary", use_container_width=True)

# ------------------- RIGHT COLUMN: OUTPUT -------------------
with col2:
    st.markdown('<p class="column-header">📊 Output</p>', unsafe_allow_html=True)

    if analyze_button:
        try:
            with st.spinner("Detecting padyam type..."):
                result = find_padyam(
                    data=padyam,
                    return_micro_score=True,
                    return_type_wise_score=True
                )

            if not result:
                st.warning("⚠️ No matching padyam type found.")
            else:
                # Sort descending by chandassu score (first element of each entry)
                result_sorted = sorted(result, key=lambda x: x[0], reverse=True)

                # Top score highlight
                st.markdown(
                    f"<div class='result-box'><h1 style='text-align:center;color:#2E8B57;margin:0;'>"
                    f"{result_sorted[0][2]}</h1>"
                    f"<p style='text-align:center;color:#555;margin:0;'><b>{result_sorted[0][0]*100:.2f}%</b></p></div>",
                    unsafe_allow_html=True
                )

                # Build table: Type | Chandassu Score | micro scores...
                updated_label = {
                    "n_paadalu": "N Paadalu (N Lines)",
                    "gana_kramam": "Gana Kramam (Syllabic Sequence)",
                    "yati_sthanam": "Yati Sthanam (Caesura Position)",
                    "n_aksharalu": "N Aksharalu (N Character Tokens)",
                    "prasa": "Prasa (Alliteration)"
                }

                rows = []
                for score, micro, ptype in result_sorted:
                    row = {"Chandassu Type": ptype, "Chandassu Score (%)": round(score * 100, 2)}
                    for key, val in micro.items():
                        label = updated_label.get(key, key.replace("_", " ").title())
                        row[label] = round(val * 100, 2)
                    rows.append(row)

                df = pd.DataFrame(rows)

                # Columns that hold percentage-style numbers -> always show 2 decimals
                score_cols = [c for c in df.columns if c != "Chandassu Type"]

                st.markdown("#### 📈 All Detected Types (Descending Score)")
                st.dataframe(
                    df.style
                        .background_gradient(subset=["Chandassu Score (%)"], cmap="Greens")
                        .format({col: "{:.2f}" for col in score_cols}),
                    use_container_width=True,
                    hide_index=True
                )

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