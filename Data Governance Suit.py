import streamlit as st
import base64

def set_bg_from_local(png_file):
    with open(png_file, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

img_base64 = set_bg_from_local("landing-page-image.png")

st.set_page_config(layout="wide")

st.markdown(f"""
    <style>
            @font-face {{ font-family: 'aeonik'; 
                        /* The name you'll use in CSS */ 
                        src: url('./fonnts.com-4556/fonts/fonnts.com-Aeonik-Regular.ttf') format('woff2');
                         /* Path to your font */
            }}
        header {{visibility: hidden;}}
        body, .stApp, #root, .main, .block-container {{
            margin-top: 0px !important;
            margin-bottom: 0px !important;
            margin-left: 0px !important;
            margin-right: 0px !important;
            padding-top: 0px !important;
            padding-bottom: 0px !important;
            padding-left: 0px !important;
            padding-right: 0px !important;
        }}
        .block-container {{
            padding-top: 1rem !important; 
            padding-left: 0rem; 
            padding-right: 0rem;
            }}
        #root > div:nth-child(1) > div > div > div > div > section > div {{
            padding-top: 0rem;
        }}

        /* Header bar full width */
        .custom-header {{
            position: fixed;
            top: 0;
            # left: 0;
            width: 100vw;
            z-index: 1000;
            left: 0;
            width: 100vw;
            height: 80px;
            background: linear-gradient(180deg, #6939f9cc 85%, #452befcc 100%);
            color: #fff;
            # font-weight: 700;
            display: flex;
            align-items: center;
            justify-content: space-between;
            letter-spacing: 2px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.10);
            gap : 1px;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;

        }}
        
        .product_title {{
          font-size: 2.1rem;
          text-transform: uppercase;
          font-weight: 500;

        }}
        .header_left {{
            margin-left : 4rem;
            font-size: 2.1rem;
                      # font-weight: 500;

        }}
            .header_right {{
            margin-right : 4rem;
                        font-size: 1.8rem;

        }}
        .stApp > .main {{
            padding-top: 70px !important; /* match header height */
        }}
        .description {{
            margin-top : 4rem;
            margin-left : 4rem;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 1.15rem;
        }}

        /* Background image */
        .stApp {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            min-height: 100vh;
        }}

        /* Shared styling for containers holding the lists */
        .feature-container {{
            # background: rgba(255,255,255,0.82);
            # border-radius: 0.6rem;
            padding: 1rem ;
            # margin-top: 1rem;
            max-width:250px
            width : 100px;
            # box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            color : #0000FF;
        }}

        /* Styling for the list items */
        ul.feature-list {{
            padding-left: 1rem;
        }}
      

        ul.feature-list li {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 1.25rem;
            color:#d43a7c;
            margin-bottom: 0.6rem;
            width: 25rem;
            font-weight: 600;
            
        }}

        /* Styling for description paragraphs inside the list */
        p.feature-desc {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            font-size: 1.15rem;
            color: #0000FF;
            # color : #04a7cb;
            text-align: justify;
            # margin: 0 0 10px 15px;
            # padding-left: 0.5rem;
        }}

    </style>
""", unsafe_allow_html=True)

# Header at the top
st.markdown("""<div class="custom-header">
            <div class="header_left"> Synthlake</div>
            <div class="product_title">Data Governance Suite</div>
            <div class="header_right"> AI, The Easy Way.</div>  </div>""", unsafe_allow_html=True)


st.markdown("""
 <div class="description" >
              <p>djfa hahfdja kkhffdajb afbajf  kafbiabfdj akfbkajbf afkjkabf kafkbjad fkabfbas afkbajbk </p>
            </div>
<div style="display: flex; flex-direction: row;  ">
  <div class="feature-container" style="margin-left: 3rem;">
    <ul class="feature-list">
      <li>Data Profiling
        <p class="feature-desc">AI driven automated data profile generation. </p>
      </li>
      <li>Data Classification
        <p class="feature-desc">Automated and manual data classification. </p>
      </li>
      <li>Data Dictionary
        <p class="feature-desc"> AI driven data dictionary generation by fine tuned AI models. </p>
      </li>
      <li>Data Lineage
        <p class="feature-desc">Complete data-lake lineage can be maintained centrally in snowflake.</p>
      </li>
    </ul>
  </div>
  <div style="flex: 1;"></div>
  <div class="feature-container" style="margin-right: 3rem; ">
    <ul class="feature-list">
      <li>Data Quality
        <p class="feature-desc">Automated data quality checks can be enabled across all data assets. </p>
      </li>
      <li>Data Unification
        <p class="feature-desc">AI driven data unification across all source systems data. </p>
      </li>
      <li>Data Observability
        <p class="feature-desc">Enable and track  data freshness, volume, distribution and schema. </p>
      </li>
      <li>Business Glossary
        <p class="feature-desc">AI driven Business Glossary generation. </p>
      </li>
    </ul>
  </div>
</div>
""", unsafe_allow_html=True)
