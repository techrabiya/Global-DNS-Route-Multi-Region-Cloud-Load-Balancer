import streamlit as st

st.title("🌐 Rabia's Global DNS Load Balancer")
st.write("Simulate multi-region traffic routing, latency checks, and server failovers.")

region = st.selectbox("Select Target Region", ["Asia-Mumbai (AP-South)", "US-East (Virginia)", "EU-Central (Frankfurt)"])

if st.button("Execute Latency Test"):
    if "Mumbai" in region:
        st.success(f"🟢 Route: {region} | Latency: 14ms | Status: Active Primary")
    else:
        st.success(f"🟡 Route: {region} | Latency: 112ms | Status: Secondary Backup")
