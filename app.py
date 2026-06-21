import streamlit as st

from agents import assemble_crew

tech_crew = assemble_crew()

st.title("Multi-Agent Software Application Development Assistant")
st.write("Have a project idea? Let our multi-agent system help you plan, develop, test, review and deploy it!")

project_idea = st.text_area("Enter your project idea here")

if "outputs" not in st.session_state:
    st.session_state.outputs = {}

if st.button("Start Development"):
    if not project_idea:
        st.error("Please enter a project idea")
    else:
        with st.spinner("Project Development in Process..."):
            result = tech_crew.kickoff(
                inputs={"project_idea": project_idea}
            )
        st.session_state.outputs = {
            "Planner": result.tasks_output[0].raw,
            "Developer": result.tasks_output[1].raw,
            "Tester": result.tasks_output[2].raw,
            "Reviewer": result.tasks_output[3].raw
        }
        st.success("Project Development Completed!")
            
        if st.session_state.outputs:
            st.subheader("Initial Project Development Results")
            tab1, tab2, tab3, tab4 = st.tabs(["Planner", "Developer", "Tester", "Reviewer"])

            with tab1:
                st.markdown(st.session_state.outputs["Planner"])
            with tab2:
                st.markdown(st.session_state.outputs["Developer"])
            with tab3:
                st.markdown(st.session_state.outputs["Tester"])
            with tab4:
                st.markdown(st.session_state.outputs["Reviewer"])

            for role, content in st.session_state.outputs.items():
                st.download_button(
                    label=f"Download {role} Document",
                    data=content,
                    file_name=f"{role.lower()}_document.md",
                    mime="text/markdown"
                )
