import streamlit as st

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, rgb(255, 167, 143), #feb47b);
        color: white;
    }
    .stApp {
        background: linear-gradient(to right, rgb(156, 68, 45), rgb(25, 55, 136));
        color: #ffffff;
        border-radius: 10px;
        padding: 20px;
    }
    h1 {
        text-align: center;
        color: rgb(236, 217, 217);
        font-size: 24px;
        font-weight: bold;
    }
    p {
        font-size: 18px;
        color: white;
        text-align: center;
    }
    .stButton>button {
        background-image: linear-gradient(135deg, #008aff, #86d472);
        border-radius: 6px;
        color: #ffffff;
        height: 50px;
        font-size: 1.2em;
        font-weight: 600;
        padding: 8px;
        width: 100%;
        text-align: center;
        margin: 10px auto;
        display: block;
    }
    .stButton>button:hover {
        color: #fff;
    }
    .result {
        background: linear-gradient(to right, rgb(250, 64, 31), rgb(184, 194, 199));
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        padding: 15px;
        border-radius: 10px;
        margin-top: 15px;
    }
    .footer {
        text-align: center;
        font-size: 16px;
        font-weight: bold;
        padding: 10px;
        color: #ffffff;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1> ⚡ Smart Unit Converter</h1>", unsafe_allow_html=True)
st.write("<p> Easily convert units from one to another </p>", unsafe_allow_html=True)

conversion_type = st.selectbox("Select the conversion type", ["Length", "Weight", "Temperature", "Volume"])
value = st.number_input("Enter the value to convert", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

if conversion_type == "Length":
    with col1:
        from_unit = st.selectbox("From", ["m", "cm", "mm", "km", "ft", "in", "mi"])
    with col2:
        to_unit = st.selectbox("To", ["m", "cm", "mm", "km", "ft", "in", "mi"])

elif conversion_type == "Weight":
    with col1:
        from_unit = st.selectbox("From", ["kg", "g", "mg", "lb", "oz"])
    with col2:
        to_unit = st.selectbox("To", ["kg", "g", "mg", "lb", "oz"])

elif conversion_type == "Temperature":
    with col1:
        from_unit = st.selectbox("From", ["C", "F", "K"])
    with col2:
        to_unit = st.selectbox("To", ["C", "F", "K"])

elif conversion_type == "Volume":
    with col1:
        from_unit = st.selectbox("From", ["L", "ml", "gal", "pt", "qt", "cup", "tbsp", "tsp"])
    with col2:
        to_unit = st.selectbox("To", ["L", "ml", "gal", "pt", "qt", "cup", "tbsp", "tsp"])

def convert_length(value, from_unit, to_unit):
    length_conversion = {
        "m": 1.0, "cm": 0.01, "mm": 0.001, "km": 1000.0,
        "ft": 0.3048, "in": 0.0254, "mi": 1609.34
    }
    return value * length_conversion[from_unit] / length_conversion[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversion = {
        "kg": 1.0, "g": 0.001, "mg": 0.000001, "lb": 0.453592, "oz": 0.0283495
    }
    return value * weight_conversion[from_unit] / weight_conversion[to_unit]

def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("C", "F"): lambda v: (v * 9/5) + 32,
        ("F", "C"): lambda v: (v - 32) * 5/9,
        ("C", "K"): lambda v: v + 273.15,
        ("K", "C"): lambda v: v - 273.15,
        ("F", "K"): lambda v: (v + 459.67) * 5/9,
        ("K", "F"): lambda v: (v * 9/5) - 459.67,
    }
    return conversions.get((from_unit, to_unit), lambda v: v)(value)

def convert_volume(value, from_unit, to_unit):
    volume_conversion = {
        "L": 1.0, "ml": 0.001, "gal": 3.78541, "pt": 0.473176,
        "qt": 0.946353, "cup": 0.236588, "tbsp": 0.014787, "tsp": 0.004929
    }
    return value * volume_conversion[from_unit] / volume_conversion[to_unit]

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.button("Convert"):
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif conversion_type == "Volume":
            result = convert_volume(value, from_unit, to_unit)

        st.markdown(
            f"""
            <div class="result">
                Result: {result} {to_unit}
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown(
    """
    <div class="footer">
        Thank you for using the unit converter! <br>
        Made with ❤️ by <strong>IQra Waqas</strong>
    </div>
    """,
    unsafe_allow_html=True
)
