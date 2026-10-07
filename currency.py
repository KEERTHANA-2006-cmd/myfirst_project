import streamlit as st
import requests

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Keerthana Currency Converter",
    page_icon="💱",
    layout="centered"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #667eea 0%,
        #764ba2 50%,
        #6b21a8 100%
    );
    min-height: 100vh;
}

/* Main content */
.block-container {
    max-width: 900px;
    padding-top: 40px;
    padding-bottom: 40px;
}

/* Title */
.main-title {
    text-align: center;
    color: white;
    font-size: 46px;
    font-weight: 800;
    margin-bottom: 5px;
    text-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #f3f4f6;
    font-size: 18px;
    margin-bottom: 35px;
}

/* Converter Card */
.converter-card {
    background: rgba(255, 255, 255, 0.97);
    padding: 35px;
    border-radius: 28px;
    box-shadow: 0px 15px 40px rgba(0, 0, 0, 0.25);
    margin-bottom: 25px;
}

/* Section title */
.section-title {
    color: #4c1d95;
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 20px;
}

/* Result Card */
.result-card {
    background: linear-gradient(
        135deg,
        #4f46e5,
        #7c3aed
    );
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-top: 25px;
    box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.25);
}

/* Result heading */
.result-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 10px;
}

/* Result amount */
.result-amount {
    font-size: 42px;
    font-weight: 800;
    margin: 10px 0;
}

/* Exchange rate */
.exchange-rate {
    font-size: 17px;
    margin-top: 15px;
}

/* Footer */
.footer {
    text-align: center;
    color: white;
    font-size: 14px;
    margin-top: 30px;
    opacity: 0.9;
}

/* Info cards */
.info-card {
    background: rgba(255, 255, 255, 0.15);
    color: white;
    padding: 18px;
    border-radius: 18px;
    text-align: center;
    margin-top: 15px;
}

/* Button */
.stButton > button {
    width: 100%;
    border-radius: 15px;
    height: 50px;
    font-size: 18px;
    font-weight: 700;
    border: none;
    background: linear-gradient(
        135deg,
        #6366f1,
        #8b5cf6
    );
    color: white;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
    box-shadow: 0px 8px 20px rgba(0, 0, 0, 0.25);
}

/* Input boxes */
div[data-baseweb="input"] {
    border-radius: 12px;
}

/* Select boxes */
div[data-baseweb="select"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.markdown(
    '<div class="main-title">💱 Keerthana Currency Converter</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    '🌎 Convert currencies quickly and easily using exchange rates'
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# CURRENCY DATA
# =========================================================

currencies = {
    "🇮🇳 INR - Indian Rupee": "INR",
    "🇺🇸 USD - US Dollar": "USD",
    "🇪🇺 EUR - Euro": "EUR",
    "🇬🇧 GBP - British Pound": "GBP",
    "🇯🇵 JPY - Japanese Yen": "JPY",
    "🇦🇺 AUD - Australian Dollar": "AUD",
    "🇨🇦 CAD - Canadian Dollar": "CAD",
    "🇨🇭 CHF - Swiss Franc": "CHF",
    "🇨🇳 CNY - Chinese Yuan": "CNY",
    "🇸🇬 SGD - Singapore Dollar": "SGD",
    "🇦🇪 AED - UAE Dirham": "AED",
    "🇸🇦 SAR - Saudi Riyal": "SAR",
    "🇰🇷 KRW - South Korean Won": "KRW",
    "🇳🇿 NZD - New Zealand Dollar": "NZD",
    "🇭🇰 HKD - Hong Kong Dollar": "HKD",
    "🇹🇭 THB - Thai Baht": "THB",
    "🇿🇦 ZAR - South African Rand": "ZAR"
}

# =========================================================
# CONVERTER CARD
# =========================================================

st.markdown(
    '<div class="converter-card">',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">💰 Currency Conversion</div>',
    unsafe_allow_html=True
)

# Amount
amount = st.number_input(
    "💵 Enter Amount",
    min_value=0.01,
    value=100.00,
    step=1.00,
    format="%.2f"
)

# Currency selection
col1, col2 = st.columns(2)

with col1:

    from_currency_name = st.selectbox(
        "🔄 From Currency",
        list(currencies.keys()),
        index=0
    )

with col2:

    to_currency_name = st.selectbox(
        "🎯 To Currency",
        list(currencies.keys()),
        index=1
    )

# Convert button
convert_button = st.button(
    "💱 CONVERT NOW"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)

# =========================================================
# CONVERSION LOGIC
# =========================================================

if convert_button:

    from_currency = currencies[from_currency_name]
    to_currency = currencies[to_currency_name]

    # Same currency
    if from_currency == to_currency:

        converted_amount = amount

        st.markdown(
            f"""
            <div class="result-card">

                <div class="result-title">
                    ✨ Converted Amount
                </div>

                <div class="result-amount">
                    {converted_amount:,.2f} {to_currency}
                </div>

                <div class="exchange-rate">
                    You selected the same currency.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        try:

            # API URL
            url = (
                f"https://api.frankfurter.app/latest"
                f"?amount={amount}"
                f"&from={from_currency}"
                f"&to={to_currency}"
            )

            # Send request
            response = requests.get(
                url,
                timeout=10
            )

            # Check response
            if response.status_code == 200:

                data = response.json()

                # Get converted value
                converted_amount = data["rates"][to_currency]

                # Calculate exchange rate
                exchange_rate = converted_amount / amount

                # Display result
                st.markdown(
                    f"""
                    <div class="result-card">

                        <div class="result-title">
                            ✨ Conversion Result
                        </div>

                        <div class="result-amount">
                            {converted_amount:,.2f} {to_currency}
                        </div>

                        <hr>

                        <div class="exchange-rate">
                            💰 {amount:,.2f} {from_currency}
                            =
                            <strong>
                                {converted_amount:,.2f} {to_currency}
                            </strong>
                        </div>

                        <div class="exchange-rate">
                            📈 1 {from_currency}
                            =
                            {exchange_rate:,.4f} {to_currency}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.error(
                    "❌ Unable to get exchange rates. "
                    "Please try again later."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "🌐 No internet connection. "
                "Please check your internet connection."
            )

        except requests.exceptions.Timeout:

            st.error(
                "⏳ The request took too long. "
                "Please try again."
            )

        except Exception as error:

            st.error(
                f"❌ Something went wrong: {error}"
            )

# =========================================================
# INFORMATION CARDS
# =========================================================

st.markdown(
    """
    <div class="info-card">
        🌎 <strong>Multiple Currencies</strong><br>
        Convert between major currencies around the world.
    </div>

    <div class="info-card">
        ⚡ <strong>Fast Conversion</strong><br>
        Get your converted amount within seconds.
    </div>

    <div class="info-card">
        📈 <strong>Exchange Rate</strong><br>
        View the exchange rate used for your conversion.
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">

        💜 Keerthana Currency Converter

        <br>

        🌎 Fast • Simple • Beautiful • User Friendly

        <br><br>

        Made with ❤️ using Streamlit

    </div>
    """,
    unsafe_allow_html=True
)