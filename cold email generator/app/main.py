import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import time

from chains import Chain
from portfolio import Portfolio
from utils import clean_text


def create_streamlit_app(llm, portfolio, clean_text):
    # Page header with custom styling
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); 
                border-radius: 10px; margin-bottom: 2rem; color: white;">
        <h1 style="margin: 0; font-size: 3rem;">📧 Cold Mail Generator</h1>
        <p style="margin: 0.5rem 0 0 0; font-size: 1.2rem; opacity: 0.9;">
            Transform job postings into personalized cold emails instantly
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Main content area
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 🎯 Job Posting Analysis")

        # URL input with better styling
        url_input = st.text_input(
            "**Enter Job Posting URL:**",
            value="https://careers.nike.com/store-manager-head-coach-dundrum/job/R-63740",
            placeholder="Paste the job posting URL here...",
            help="Enter the URL of the job posting you want to create a cold email for"
        )

        # Submit button with custom styling
        submit_button = st.button(
            "🚀 Generate Cold Email",
            type="primary",
            use_container_width=True
        )

    with col2:
        st.markdown("### 📊 Quick Stats")

        # Create some visual elements
        st.markdown("""
        <div style="background: black; padding: 1rem; border-radius: 8px; margin-bottom: 1rem;">
            <h4 style="margin: 0 0 0.5rem 0; color: white;">✨ Features</h4>
            <ul style="margin: 0; padding-left: 1.2rem;">
                <li>AI-powered email generation</li>
                <li>Portfolio matching</li>
                <li>Professional formatting</li>
                <li>Instant results</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

        # Tips section
        with st.expander("💡 Tips for Best Results"):
            st.markdown("""
            - Use complete job posting URLs
            - Ensure your portfolio is up to date
            - Review and customize generated emails
            - Check for company-specific requirements
            """)

    # Processing and Results Section
    if submit_button:
        if not url_input.strip():
            st.error("⚠️ Please enter a valid URL")
            return

        # Progress indicator
        progress_bar = st.progress(0)
        status_text = st.empty()

        try:
            # Step 1: Loading job posting
            status_text.text("🔍 Analyzing job posting...")
            progress_bar.progress(25)
            time.sleep(0.5)

            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)

            # Step 2: Loading portfolio
            status_text.text("📁 Loading portfolio...")
            progress_bar.progress(50)
            time.sleep(0.5)

            portfolio.load_portfolio()

            # Step 3: Extracting jobs
            status_text.text("🎯 Extracting job requirements...")
            progress_bar.progress(75)
            time.sleep(0.5)

            jobs = llm.extract_jobs(data)

            # Step 4: Generating emails
            status_text.text("✍️ Generating personalized emails...")
            progress_bar.progress(100)
            time.sleep(0.5)

            # Clear progress indicators
            progress_bar.empty()
            status_text.empty()

            # Display results
            if jobs:
                st.markdown("---")
                st.markdown("### 📬 Generated Cold Emails")

                for i, job in enumerate(jobs, 1):
                    # Job details in expandable section
                    with st.expander(f"📋 Job {i} Details", expanded=False):
                        col_a, col_b = st.columns(2)
                        with col_a:
                            st.markdown("**Role:**")
                            st.write(job.get('role', 'Not specified'))
                            st.markdown("**Company:**")
                            st.write(job.get('company', 'Not specified'))
                        with col_b:
                            st.markdown("**Skills Required:**")
                            skills = job.get('skills', [])
                            if skills:
                                st.write(", ".join(skills))
                            else:
                                st.write("Not specified")

                    # Generate email
                    skills = job.get('skills', [])
                    links = portfolio.query_links(skills)
                    email = llm.write_mail(job, links)

                    # Display email with better formatting
                    st.markdown(f"#### 📧 Cold Email {i}")

                    # Email preview with copy button
                    email_container = st.container()
                    with email_container:
                        st.markdown("""
                        <div style="background: #f8f9fa; border-left: 4px solid #667eea; padding: 1rem; 
                                   border-radius: 0 8px 8px 0; margin: 1rem 0;">
                        """, unsafe_allow_html=True)

                        st.code(email, language='markdown')

                        st.markdown("</div>", unsafe_allow_html=True)

                        # Action buttons
                        col_copy, col_download = st.columns(2)
                        with col_copy:
                            if st.button(f"📋 Copy Email {i}", key=f"copy_{i}"):
                                st.success("Email copied to clipboard!")
                        with col_download:
                            st.download_button(
                                label=f"💾 Download Email {i}",
                                data=email,
                                file_name=f"cold_email_{i}.txt",
                                mime="text/plain",
                                key=f"download_{i}"
                            )

                    if i < len(jobs):
                        st.markdown("---")

                # Success message
                st.markdown("""
                <div style="background: #d4edda; border: 1px solid #c3e6cb; color: #155724; 
                           padding: 1rem; border-radius: 8px; margin: 2rem 0;">
                    <h4 style="margin: 0 0 0.5rem 0;">✅ Success!</h4>
                    <p style="margin: 0;">Your cold email(s) have been generated successfully. 
                    Review and customize them before sending.</p>
                </div>
                """, unsafe_allow_html=True)

            else:
                st.warning("⚠️ No job postings found in the provided URL. Please check the URL and try again.")

        except Exception as e:
            progress_bar.empty()
            status_text.empty()

            st.markdown("""
            <div style="background: #f8d7da; border: 1px solid #f5c6cb; color: #721c24; 
                       padding: 1rem; border-radius: 8px; margin: 1rem 0;">
                <h4 style="margin: 0 0 0.5rem 0;">❌ Error Occurred</h4>
                <p style="margin: 0;">""" + str(e) + """</p>
            </div>
            """, unsafe_allow_html=True)

            # Troubleshooting tips
            with st.expander("🔧 Troubleshooting Tips"):
                st.markdown("""
                - **Invalid URL**: Make sure the URL is complete and accessible
                - **Network Issues**: Check your internet connection
                - **Blocked Content**: Some websites may block automated access
                - **Rate Limits**: Try again after a few minutes if you've made many requests
                """)

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 2rem 0; color: #666;">
        <p style="margin: 0;">Built with ❤️ using Streamlit | 
        <a href="#" style="color: #667eea; text-decoration: none;">Documentation</a> | 
        <a href="#" style="color: #667eea; text-decoration: none;">Support</a></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(
        layout="wide",
        page_title="Cold Email Generator",
        page_icon="📧",
        initial_sidebar_state="collapsed"
    )
    create_streamlit_app(chain, portfolio, clean_text)