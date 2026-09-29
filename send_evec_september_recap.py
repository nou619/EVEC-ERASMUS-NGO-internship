import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


# ============================================================
# 1. LOAD EMAIL SETTINGS FROM .env
# ============================================================

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

if not all([EMAIL_ADDRESS, EMAIL_APP_PASSWORD, RECIPIENT_EMAIL]):
    raise ValueError(
        "Missing EMAIL_ADDRESS, EMAIL_APP_PASSWORD, or RECIPIENT_EMAIL in .env"
    )


# ============================================================
# 2. CREATE EMAIL
# ============================================================

message = EmailMessage()

message["From"] = EMAIL_ADDRESS
message["To"] = RECIPIENT_EMAIL
message["Subject"] = "🌱 EVEC Microgreens Research — September Recap"

# Plain-text fallback
message.set_content(
    """
EVEC Microgreens Market Research
September 2026 Monthly Research Recap

This email contains an HTML research dashboard.
Please open it in an email client that supports HTML.
"""
)


# ============================================================
# 3. COMPLETE HTML EMAIL
# ============================================================

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body style="
    margin:0;
    padding:0;
    background-color:#f3f6f4;
    font-family:Arial,Helvetica,sans-serif;
    color:#1f2923;
">

<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="background-color:#f3f6f4;"
>
<tr>
<td align="center" style="padding:28px 12px;">

<table
    width="680"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="
        width:100%;
        max-width:680px;
        background-color:#ffffff;
        border-radius:18px;
        overflow:hidden;
    "
>

<!-- ====================================================== -->
<!-- HEADER -->
<!-- ====================================================== -->

<tr>
<td style="
    background-color:#153d2a;
    padding:38px;
    color:#ffffff;
">

<div style="
    font-size:12px;
    font-weight:bold;
    letter-spacing:2px;
    color:#b9ddc7;
">
    EVEC · ATHENS
</div>

<h1 style="
    margin:10px 0 6px 0;
    font-size:30px;
    line-height:1.2;
    color:#ffffff;
">
    🌱 Microgreens Market Research
</h1>

<div style="
    font-size:16px;
    color:#dcebe2;
">
    September 2026 · Monthly Research Recap
</div>

<p style="
    margin:22px 0 0 0;
    font-size:15px;
    line-height:1.7;
    color:#eef6f1;
">
    This month I focused on identifying which public data sources can
    actually answer the five questions in the project, testing what can
    realistically be automated, and starting to build the market evidence
    from sources specific enough to be useful.
</p>

</td>
</tr>


<!-- ====================================================== -->
<!-- BODY -->
<!-- ====================================================== -->

<tr>
<td style="padding:34px 34px 10px 34px;">


<!-- ====================================================== -->
<!-- AT A GLANCE -->
<!-- ====================================================== -->

<div style="
    font-size:12px;
    font-weight:bold;
    letter-spacing:1.5px;
    color:#6d7771;
    margin-bottom:14px;
">
    SEPTEMBER AT A GLANCE
</div>

<table width="100%" cellpadding="0" cellspacing="0" border="0">
<tr>

<td width="24%" valign="top" style="padding-right:6px;">
<div style="
    background-color:#eaf7ee;
    border-radius:12px;
    padding:16px 10px;
    text-align:center;
">
    <div style="
        font-size:24px;
        font-weight:bold;
        color:#17663a;
    ">
        8+
    </div>

    <div style="
        font-size:11px;
        line-height:1.4;
        color:#536159;
        margin-top:5px;
    ">
        seller / producer leads
    </div>
</div>
</td>


<td width="24%" valign="top" style="padding:0 3px;">
<div style="
    background-color:#eaf7ee;
    border-radius:12px;
    padding:16px 10px;
    text-align:center;
">
    <div style="
        font-size:24px;
        font-weight:bold;
        color:#17663a;
    ">
        €3.90
    </div>

    <div style="
        font-size:11px;
        line-height:1.4;
        color:#536159;
        margin-top:5px;
    ">
        25g retail benchmark
    </div>
</div>
</td>


<td width="24%" valign="top" style="padding:0 3px;">
<div style="
    background-color:#eaf7ee;
    border-radius:12px;
    padding:16px 10px;
    text-align:center;
">
    <div style="
        font-size:24px;
        font-weight:bold;
        color:#17663a;
    ">
        30
    </div>

    <div style="
        font-size:11px;
        line-height:1.4;
        color:#536159;
        margin-top:5px;
    ">
        varieties claimed by one producer
    </div>
</div>
</td>


<td width="28%" valign="top" style="padding-left:6px;">
<div style="
    background-color:#fff5d9;
    border-radius:12px;
    padding:16px 10px;
    text-align:center;
">
    <div style="
        font-size:24px;
        font-weight:bold;
        color:#966900;
    ">
        3
    </div>

    <div style="
        font-size:11px;
        line-height:1.4;
        color:#665c45;
        margin-top:5px;
    ">
        official-data routes investigated
    </div>
</div>
</td>

</tr>
</table>


<!-- ====================================================== -->
<!-- COMPETITORS -->
<!-- ====================================================== -->

<div style="
    margin-top:34px;
    background-color:#eaf7ee;
    border-left:5px solid #28a45f;
    border-radius:10px;
    padding:22px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    color:#23784a;
">
    🟢 STRONGEST PROGRESS
</div>

<h2 style="
    margin:6px 0 12px 0;
    font-size:21px;
">
    1 · Competitors & existing supply
</h2>

<p style="
    font-size:14px;
    line-height:1.7;
    margin:0;
">
    I identified and started mapping Greek microgreens businesses including
    <b>FoodsCross, Gourmet Leaves, Micro Miracles / I Akri Tou Kipou,
    MicroGreenPlants, Microgreens Greece / Hy-Farm and CityGreens</b>,
    along with additional leads still being checked.
</p>

<p style="
    font-size:14px;
    line-height:1.7;
    margin:14px 0 0 0;
">
    The dataset is being structured as:
    <b>seller → location → varieties → pack size → price → €/g →
    delivery → customer type → source.</b>
</p>

</div>


<!-- ====================================================== -->
<!-- PUBLIC EVIDENCE -->
<!-- ====================================================== -->

<h3 style="
    margin:28px 0 12px 0;
    font-size:16px;
">
    What the public evidence already tells us
</h3>

<table width="100%" cellpadding="0" cellspacing="0" border="0">

<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
    line-height:1.6;
">
    <b>Gourmet Leaves</b><br>

    <span style="color:#5f6963;">
        Public information describes roughly 30 microgreen varieties grown
        year-round and production aimed at chefs and restaurants.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
    line-height:1.6;
">
    <b>Microgreens Greece</b><br>

    <span style="color:#5f6963;">
        States that it distributes microgreens and edible flowers and serves
        dozens of HORECA businesses.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    font-size:14px;
    line-height:1.6;
">
    <b>Micro Miracles</b><br>

    <span style="color:#5f6963;">
        Publicly advertises Athens delivery within 24 hours after harvest.
    </span>
</td>
</tr>

</table>


<!-- ====================================================== -->
<!-- PRICES -->
<!-- ====================================================== -->

<div style="
    margin-top:30px;
    background-color:#eaf7ee;
    border-left:5px solid #28a45f;
    border-radius:10px;
    padding:22px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    color:#23784a;
">
    🟢 REAL MARKET DATA
</div>

<h2 style="
    margin:6px 0 14px 0;
    font-size:21px;
">
    2 · Public price signals
</h2>

<p style="
    font-size:14px;
    line-height:1.7;
">
    Instead of relying only on market estimates, I found public Greek
    product prices that can be converted into comparable €/g benchmarks.
</p>

<table
    width="100%"
    cellpadding="8"
    cellspacing="0"
    border="0"
    style="
        font-size:13px;
        background-color:#ffffff;
        border-radius:8px;
    "
>

<tr style="background-color:#dff1e5;">
    <td><b>Seller</b></td>
    <td><b>Product</b></td>
    <td><b>Weight</b></td>
    <td><b>Price</b></td>
</tr>

<tr>
    <td>FoodsCross</td>
    <td>Multiple varieties</td>
    <td>25g</td>
    <td><b>€3.90</b></td>
</tr>

<tr>
    <td>Micro Miracles</td>
    <td>Salad Mix</td>
    <td>100g</td>
    <td><b>€4.00</b></td>
</tr>

<tr>
    <td>Micro Miracles</td>
    <td>Sunflower</td>
    <td>100g</td>
    <td><b>€4.00</b></td>
</tr>

<tr>
    <td>Micro Miracles</td>
    <td>Radish</td>
    <td>100g</td>
    <td><b>€4.00</b></td>
</tr>

<tr>
    <td>Micro Miracles</td>
    <td>Rainbow Mix</td>
    <td>100g</td>
    <td><b>€9.00</b></td>
</tr>

<tr>
    <td>Micro Miracles</td>
    <td>Red Mustard</td>
    <td>25g</td>
    <td><b>€3.50</b></td>
</tr>

</table>

<p style="
    font-size:12px;
    line-height:1.6;
    color:#647068;
    margin:14px 0 0 0;
">
    ⚠️ These are public retail/product benchmarks. They should not be
    interpreted as restaurant wholesale prices.
</p>

</div>


<!-- ====================================================== -->
<!-- BUYERS -->
<!-- ====================================================== -->

<div style="
    margin-top:30px;
    background-color:#fff7df;
    border-left:5px solid #e6ae2c;
    border-radius:10px;
    padding:22px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    color:#946b0b;
">
    🟡 BUILDING THE EVIDENCE
</div>

<h2 style="
    margin:6px 0 12px 0;
    font-size:21px;
">
    3 · Who actually buys microgreens?
</h2>

<p style="
    font-size:14px;
    line-height:1.7;
">
    I am keeping a strict distinction between a <b>potential buyer</b> and
    a business for which there is public evidence of actual microgreens use.
    Simply appearing on Wolt, efood or Michelin is not enough to classify
    a restaurant as a verified buyer.
</p>

<p style="
    font-size:14px;
    line-height:1.7;
">
    There is already stronger evidence that the restaurant market exists.
    Gourmet Leaves explicitly describes chefs and restaurants as customers,
    and published coverage of the producer names restaurants that have used
    its products, including <b>Artisanal, To Theio Tragi, Veri Table,
    Simul and Mystikos Kipos.</b>
</p>

<p style="
    font-size:14px;
    line-height:1.7;
    margin-bottom:0;
">
    The buyer dataset will therefore only mark a business as verified when
    a public source supports the connection.
</p>

</div>


<!-- ====================================================== -->
<!-- EUROSTAT -->
<!-- ====================================================== -->

<div style="
    margin-top:30px;
    background-color:#fff7df;
    border-left:5px solid #e6ae2c;
    border-radius:10px;
    padding:22px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    color:#946b0b;
">
    🟡 DATA LIMITATION FOUND
</div>

<h2 style="
    margin:6px 0 12px 0;
    font-size:21px;
">
    4 · The Eurostat question
</h2>

<p style="
    font-size:14px;
    line-height:1.7;
">
    I investigated whether official trade data could answer:
    <b>How much microgreens does Greece import, from where, and at what value?</b>
</p>


<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="margin:18px 0;"
>
<tr>

<td
    align="center"
    style="
        background-color:#ffffff;
        border-radius:8px;
        padding:13px;
        font-size:13px;
    "
>
    <b>EUROSTAT</b>
</td>

<td align="center" style="font-size:20px;padding:5px;">
    →
</td>

<td
    align="center"
    style="
        background-color:#ffffff;
        border-radius:8px;
        padding:13px;
        font-size:13px;
    "
>
    <b>Trade API</b><br>
    ⚙️ automatable
</td>

<td align="center" style="font-size:20px;padding:5px;">
    →
</td>

<td
    align="center"
    style="
        background-color:#fdeaea;
        border-radius:8px;
        padding:13px;
        font-size:13px;
    "
>
    <b>Product classification</b><br>
    ⚠️ too broad
</td>

</tr>
</table>


<p style="
    font-size:14px;
    line-height:1.7;
">
    <b>Automation is not the blocker.</b>
    Eurostat provides official API access to trade data.
    The limitation is product specificity: I did not establish a
    classification that isolates microgreens cleanly enough to justify
    reporting a standalone Greek microgreens import figure.
</p>


<div style="
    background-color:#ffffff;
    border-radius:8px;
    padding:15px;
    margin-top:14px;
">

<span style="
    font-size:13px;
    line-height:1.6;
">
    🔴 I therefore did <b>not</b> take a broad vegetable category and
    present it as “Greek microgreens imports.”
</span>

</div>

</div>


<!-- ====================================================== -->
<!-- AUTOMATION -->
<!-- ====================================================== -->

<h2 style="
    margin:34px 0 14px 0;
    font-size:21px;
">
    5 · What can actually be automated?
</h2>


<table
    width="100%"
    cellpadding="10"
    cellspacing="0"
    border="0"
    style="
        font-size:13px;
        border-collapse:collapse;
    "
>

<tr style="background-color:#f0f3f1;">
    <td><b>Source</b></td>
    <td><b>What happened</b></td>
    <td><b>Status</b></td>
</tr>


<tr>
<td style="border-bottom:1px solid #e5e9e6;">
    <b>Eurostat</b>
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    Official API available
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    ⚙️ Automatable
</td>
</tr>


<tr>
<td style="border-bottom:1px solid #e5e9e6;">
    <b>Seller catalogues</b>
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    Useful public product and price data
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    🟢 Collect / verify
</td>
</tr>


<tr>
<td style="border-bottom:1px solid #e5e9e6;">
    <b>Wolt / efood</b>
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    Useful menu evidence, but not treated as a guaranteed recurring
    scraping pipeline
</td>

<td style="border-bottom:1px solid #e5e9e6;">
    🟡 Evidence source
</td>
</tr>


<tr>
<td>
    <b>Broad trade categories</b>
</td>

<td>
    Cannot be treated as microgreens-specific data
</td>

<td>
    🔴 Rejected
</td>
</tr>

</table>


<!-- ====================================================== -->
<!-- RESEARCH -->
<!-- ====================================================== -->

<div style="
    margin-top:30px;
    background-color:#eef3ff;
    border-left:5px solid #6686c4;
    border-radius:10px;
    padding:22px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    color:#526da3;
">
    📚 RESEARCH SUPPORT
</div>

<h2 style="
    margin:6px 0 15px 0;
    font-size:21px;
">
    6 · Greek research relevant to EVEC
</h2>


<p style="
    font-size:14px;
    line-height:1.7;
">
    <b>Greek consumer research — 2023</b><br>
    A Hellenic Open University MSc thesis studied microgreens and potential
    consumers in Greece, using survey and statistical analysis to investigate
    factors affecting willingness to purchase.
</p>


<p style="
    font-size:14px;
    line-height:1.7;
">
    <b>Agrifood → hotel sales — 2024</b><br>
    An Agricultural University of Athens thesis developed a business plan
    around direct agrifood sales to hotel-sector businesses.
    It is useful context for EVEC's hotel sales channel, but it is not being
    treated as microgreens demand data.
</p>


<p style="
    font-size:14px;
    line-height:1.7;
    margin-bottom:0;
">
    <b>Microgreens production research</b><br>
    Greek researchers, including work connected to the Agricultural
    University of Athens, have studied hydroponic microgreens and more
    recently the effect of lighting conditions on development and yield.
    These sources may support production and tray-economics assumptions later.
</p>

</div>


<!-- ====================================================== -->
<!-- NEXT STAGES -->
<!-- ====================================================== -->

<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
    style="margin-top:30px;"
>
<tr>


<td
    width="49%"
    valign="top"
    style="padding-right:6px;"
>
<div style="
    background-color:#fdecec;
    border-left:4px solid #d95c5c;
    border-radius:9px;
    padding:18px;
">

<div style="
    font-size:11px;
    font-weight:bold;
    color:#ad3f3f;
">
    🔴 NEXT STAGE
</div>

<h3 style="
    margin:6px 0 8px;
    font-size:16px;
">
    Tray economics
</h3>

<p style="
    font-size:12px;
    line-height:1.6;
    margin:0;
    color:#5d6360;
">
    Seeds + substrate + trays + utilities + packaging + space → yield →
    cycle → cost/tray → margin → break-even.
</p>

</div>
</td>


<td
    width="49%"
    valign="top"
    style="padding-left:6px;"
>
<div style="
    background-color:#fdecec;
    border-left:4px solid #d95c5c;
    border-radius:9px;
    padding:18px;
">

<div style="
    font-size:11px;
    font-weight:bold;
    color:#ad3f3f;
">
    🔴 NEXT STAGE
</div>

<h3 style="
    margin:6px 0 8px;
    font-size:16px;
">
    Migrant / cooperative
</h3>

<p style="
    font-size:12px;
    line-height:1.6;
    margin:0;
    color:#5d6360;
">
    Public Greek/EU statistics, academic research and NGO/government
    sources → communities → training → crops → cooperative feasibility.
</p>

</div>
</td>

</tr>
</table>


<!-- ====================================================== -->
<!-- NEXT OUTPUTS -->
<!-- ====================================================== -->

<h2 style="
    margin:36px 0 15px;
    font-size:21px;
">
    → Next outputs
</h2>


<table
    width="100%"
    cellpadding="0"
    cellspacing="0"
    border="0"
>

<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
">
    <b style="color:#25834a;">01</b>&nbsp;&nbsp;
    <b>Athens Buyer Dataset</b><br>

    <span style="color:#667069;">
        Public evidence + source + evidence strength.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
">
    <b style="color:#25834a;">02</b>&nbsp;&nbsp;
    <b>Greek Price Dataset</b><br>

    <span style="color:#667069;">
        Seller → variety → weight → price → €/g → delivery.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
">
    <b style="color:#25834a;">03</b>&nbsp;&nbsp;
    <b>Competitor Comparison</b><br>

    <span style="color:#667069;">
        Products + positioning + pricing + strongest 2–3 competitor analysis.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    border-bottom:1px solid #e7ebe8;
    font-size:14px;
">
    <b style="color:#25834a;">04</b>&nbsp;&nbsp;
    <b>Tray Economics Calculator</b><br>

    <span style="color:#667069;">
        Cost/tray → margin → break-even, with visible assumptions.
    </span>
</td>
</tr>


<tr>
<td style="
    padding:13px 0;
    font-size:14px;
">
    <b style="color:#25834a;">05</b>&nbsp;&nbsp;
    <b>Migrant / Cooperative Research</b><br>

    <span style="color:#667069;">
        Build the final project question from public evidence.
    </span>
</td>
</tr>

</table>


<!-- ====================================================== -->
<!-- CURRENT STATUS -->
<!-- ====================================================== -->

<div style="
    margin-top:32px;
    background-color:#f5f7f5;
    border-radius:12px;
    padding:20px;
">

<div style="
    font-size:12px;
    font-weight:bold;
    letter-spacing:1px;
    color:#68726c;
    margin-bottom:12px;
">
    CURRENT STATUS
</div>

<div style="
    font-size:13px;
    line-height:2;
">
    🟢 Competitor / seller research — <b>strong progress</b><br>
    🟢 Public pricing — <b>usable data obtained</b><br>
    🟡 Buyer analysis — <b>building verified evidence</b><br>
    🟡 Import analysis — <b>method tested; classification limitation identified</b><br>
    🔴 Tray economics — <b>next stage</b><br>
    🔴 Migrant / cooperative analysis — <b>next stage</b>
</div>

</div>


<!-- ====================================================== -->
<!-- SIGNATURE -->
<!-- ====================================================== -->

<div style="padding:32px 0 25px 0;">

<div style="
    font-size:14px;
    font-weight:bold;
">
    Nour Ben Hnia
</div>

<div style="
    font-size:12px;
    color:#7a837e;
    margin-top:4px;
">
    EVEC · September 2026
</div>

</div>


</td>
</tr>
</table>

</td>
</tr>
</table>

</body>
</html>
"""


# ============================================================
# 4. ATTACH HTML AS THE EMAIL BODY
# ============================================================

message.add_alternative(html, subtype="html")


# ============================================================
# 5. SEND THROUGH GMAIL SMTP
# ============================================================

print("📨 Connecting to Gmail...")

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:

        smtp.login(
            EMAIL_ADDRESS,
            EMAIL_APP_PASSWORD
        )

        print("✅ Gmail login successful.")

        smtp.send_message(message)

    print("🌱 EVEC September recap sent successfully!")
    print(f"📬 Sent to: {RECIPIENT_EMAIL}")

except smtplib.SMTPAuthenticationError:
    print("❌ Gmail rejected the login.")
    print("Check EMAIL_ADDRESS and EMAIL_APP_PASSWORD in your .env file.")

except Exception as error:
    print("❌ Email could not be sent.")
    print(error)