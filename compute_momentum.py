import pandas as pd
import numpy as np
import yfinance as yf
import json
import time

# Cleaned constituent symbols list
symbols = [
    "360ONE.NS", "ABB.NS", "ACC.NS", "ACMESOLAR.NS", "AIAENG.NS", "APLAPOLLO.NS", "AUBANK.NS", "AWL.NS", "AXISCADES.NS", "AADHARHFC.NS",
    "AARTIIND.NS", "AARTIPHARM.NS", "AAVAS.NS", "ABBOTINDIA.NS", "ACE.NS", "ACUTAAS.NS", "ADANIENSOL.NS", "ADANIENT.NS", "ADANIGREEN.NS",
    "ADANIPORTS.NS", "ADANIPOWER.NS", "ATGL.NS", "ABCAPITAL.NS", "ABFRL.NS", "ABLBL.NS", "ABREL.NS", "ABSLAMC.NS", "CPPLUS.NS",
    "AVL.NS", "ADVENZYMES.NS", "AEGISLOG.NS", "AEGISVOPAK.NS", "AEQUS.NS", "AEROFLEX.NS", "AETHER.NS", "AFCONS.NS", "AFFLE.NS",
    "AJANTPHARM.NS", "AKUMS.NS", "ALKEM.NS", "ALKYLAMINE.NS", "ABDL.NS", "AMAGI.NS", "ARE&M.NS", "AMBER.NS", "AMBUJACEM.NS",
    "ANANDRATHI.NS", "ANANTRAJ.NS", "ANGELONE.NS", "ANTHEM.NS", "ANURAS.NS", "APARINDS.NS", "APOLLOHOSP.NS", "APOLLO.NS", "APOLLOTYRE.NS",
    "APTUS.NS", "ACI.NS", "ARVINDFASN.NS", "ARVIND.NS", "ASAHIINDIA.NS", "ASHAPURMIN.NS", "ASHOKLEY.NS", "ASHOKA.NS", "ASIANPAINT.NS",
    "ASTERDM.NS", "ASTRAMICRO.NS", "ASTRAL.NS", "ATHERENERG.NS", "ATLANTAELE.NS", "ATUL.NS", "AURIONPRO.NS", "AUROPHARMA.NS",
    "AIIL.NS", "AVALON.NS", "AVANTIFEED.NS", "DMART.NS", "CCAVENUE.NS", "AXISBANK.NS", "AZAD.NS", "BEML.NS", "BLS.NS", "BSE.NS",
    "BAJAJ-AUTO.NS", "BAJAJCON.NS", "BAJFINANCE.NS", "BAJAJFINSV.NS", "BAJAJHLDNG.NS", "BAJAJHFL.NS", "BALAMINES.NS",
    "BALKRISIND.NS", "BALRAMCHIN.NS", "BALUFORGE.NS", "BANCOINDIA.NS", "BANDHANBNK.NS", "BANKBARODA.NS", "BANKINDIA.NS", "MAHABANK.NS",
    "BATAINDIA.NS", "BELRISE.NS", "BERGEPAINT.NS", "BHARATCOAL.NS", "BDL.NS", "BEL.NS", "BHARATFORG.NS", "BHEL.NS", "BPCL.NS",
    "BHARTIARTL.NS", "BHARTIHEXA.NS", "GROWW.NS", "BIOCON.NS", "BIRLACORPN.NS", "BSOFT.NS", "BBOX.NS", "BLACKBUCK.NS", "BLUEJET.NS",
    "BLUESTARCO.NS", "BLUESTONE.NS", "BORORENEW.NS", "BOSCHLTD.NS", "FIRSTCRY.NS", "BRIGADE.NS", "BRITANNIA.NS", "BIRET.NS",
    "MAPMYINDIA.NS", "CCL.NS", "CESC.NS", "CGPOWER.NS", "CIEINDIA.NS", "CMRGREEN.NS", "CMSINFO.NS", "CRISIL.NS", "CSBBANK.NS",
    "CAMPUS.NS", "CANFINHOME.NS", "CANBK.NS", "CANHLIFE.NS", "CRAMC.NS", "CAPILLARY.NS", "CAPLIPOINT.NS", "CGCL.NS", "CARBORUNIV.NS",
    "CARTRADE.NS", "CASTROLIND.NS", "CEATLTD.NS", "CEIGALL.NS", "CELLO.NS", "CEMPRO.NS", "CENTRALBK.NS", "CDSL.NS", "CMPDI.NS",
    "CENTUM.NS", "CERA.NS", "CHALET.NS", "CHAMBLFERT.NS", "CHENNPETRO.NS", "CHOICEIN.NS", "CHOLAHLDNG.NS", "CHOLAFIN.NS", "CIPLA.NS",
    "CUB.NS", "CLEANMAX.NS", "CLEAN.NS", "COALINDIA.NS", "COCHINSHIP.NS", "COFORGE.NS", "COHANCE.NS", "COLPAL.NS", "CAMS.NS",
    "CONCORDBIO.NS", "CONCOR.NS", "COROMANDEL.NS", "CRAFTSMAN.NS", "CREDITACC.NS", "CROMPTON.NS", "CUMMINSIND.NS", "CUPID.NS",
    "CYIENT.NS", "DCBBANK.NS", "DLF.NS", "DOMS.NS", "DABUR.NS", "DALBHARAT.NS", "DATAPATTNS.NS", "DATAMATICS.NS", "DEEPAKFERT.NS",
    "DEEPAKNTR.NS", "DELHIVERY.NS", "DEVYANI.NS", "DIACABS.NS", "DBL.NS", "DIVISLAB.NS", "DIXON.NS", "LALPATHLAB.NS", "DRREDDY.NS",
    "DYNAMATECH.NS", "EIDPARRY.NS", "E2E.NS", "EIHOTEL.NS", "EMBASSY.NS", "EPL.NS", "EDELWEISS.NS", "EICHERMOT.NS", "ELECON.NS",
    "EMIL.NS", "ELECTCAST.NS", "ELGIEQUIP.NS", "ELLEN.NS", "EMAMILTD.NS", "EMBDL.NS", "EMCURE.NS", "EMMVEE.NS", "ENDURANCE.NS",
    "ENGINERSIN.NS", "ENTERO.NS", "EIEL.NS", "EQUITASBNK.NS", "ERIS.NS", "ESCORTS.NS", "ETERNAL.NS", "EXIDEIND.NS", "NYKAA.NS",
    "FEDFINA.NS", "FEDERALBNK.NS", "FACT.NS", "FIEMIND.NS", "FINCABLES.NS", "FINPIPE.NS", "FSL.NS", "FIVESTAR.NS", "FORCEMOT.NS",
    "FORTIS.NS", "FRACTAL.NS", "UTLSOLAR.NS", "GAIL.NS", "GVT&D.NS", "GMRAIRPORT.NS", "GMRP&UI.NS", "EBGNG.NS", "GABRIEL.NS",
    "GALLANTT.NS", "GRSE.NS", "GRWRHITECH.NS", "GICRE.NS", "GENUSPOWER.NS", "GILLETTE.NS", "GLAND.NS", "GLAXO.NS", "GLENMARK.NS",
    "MEDANTA.NS", "GPIL.NS", "GODFRYPHLP.NS", "GODREJAGRO.NS", "GODREJCP.NS", "GODREJIND.NS", "GODREJPROP.NS", "GOKEX.NS",
    "GOKULAGRO.NS", "GOLDIAM.NS", "GRANULES.NS", "GRAPHITE.NS", "GRASIM.NS", "GRAVITA.NS", "GESHIP.NS", "GREAVESCOT.NS",
    "GRINDWELL.NS", "GUJALKALI.NS", "GAEL.NS", "FLUOROCHEM.NS", "GMDCLTD.NS", "GNFC.NS", "GPPL.NS", "GSFC.NS", "HGINFRA.NS",
    "HBLENGINE.NS", "HCLTECH.NS", "HDBFS.NS", "HDFCAMC.NS", "HDFCBANK.NS", "HDFCLIFE.NS", "HEGAM.NS", "HFCL.NS", "HAPPSTMNDS.NS",
    "HAPPYFORGE.NS", "HAVELLS.NS", "HCG.NS", "HERITGFOOD.NS", "HEROMOTOCO.NS", "HEXT.NS", "HSCL.NS", "HINDALCO.NS", "HAL.NS",
    "HCC.NS", "HINDCOPPER.NS", "HINDPETRO.NS", "HINDUNILVR.NS", "HINDZINC.NS", "POWERINDIA.NS", "HOMEFIRST.NS", "HONASA.NS",
    "HONAUT.NS", "HUDCO.NS", "HYUNDAI.NS", "ICICIBANK.NS", "ICICIGI.NS", "ICICIAMC.NS", "ICICIPRULI.NS", "IDBI.NS", "IDFCFIRSTB.NS",
    "IFBIND.NS", "IFCI.NS", "IIFLCAPS.NS", "IIFL.NS", "INOXINDIA.NS", "IRB.NS", "IRCON.NS", "ITCHOTELS.NS", "ITC.NS", "ITI.NS",
    "INDGN.NS", "INDIACEM.NS", "INDIAGLYCO.NS", "INDIAMART.NS", "INDIANB.NS", "IEX.NS", "INDHOTEL.NS", "IMFA.NS", "IOC.NS",
    "IOB.NS", "IRCTC.NS", "IRFC.NS", "IREDA.NS", "INDIGOPNTS.NS", "ICIL.NS", "IGL.NS", "INDUSTOWER.NS", "INDUSINDBK.NS", "NAUKRI.NS",
    "INFY.NS", "INOXWIND.NS", "INTELLECT.NS", "INDIGO.NS", "IGIL.NS", "IKS.NS", "IONEXCHANG.NS", "IPCALAB.NS", "JKCEMENT.NS",
    "JAIBALAJI.NS", "JBMA.NS", "JKPAPER.NS", "JKTYRE.NS", "JMFINANCIL.NS", "JSWCEMENT.NS", "JSWENERGY.NS", "JSWINFRA.NS", "JSWSTEEL.NS",
    "JAINREC.NS", "JPPOWER.NS", "J&KBANK.NS", "JAMNAAUTO.NS", "JSFB.NS", "JAYNECOIND.NS", "JSLL.NS", "JINDALSAW.NS", "JSL.NS",
    "JINDALSTEL.NS", "JIOFIN.NS", "JUBLFOOD.NS", "JUBLINGREA.NS", "JUBLPHARMA.NS", "JWL.NS", "JUSTDIAL.NS", "JYOTHYLAB.NS",
    "JYOTICNC.NS", "KPRMILL.NS", "KEI.NS", "KNRCON.NS", "KPIGREEN.NS", "KPITTECH.NS", "KRBL.NS", "KRN.NS", "KSB.NS", "KAJARIACER.NS",
    "KPIL.NS", "KALYANKJIL.NS", "KANSAINER.NS", "KTKBANK.NS", "KARURVYSYA.NS", "KSCL.NS", "KAYNES.NS", "KEC.NS", "KFINTECH.NS",
    "KIRLOSBROS.NS", "KIRLOSENG.NS", "KIRLPNU.NS", "KITEX.NS", "KMEW.NS", "KOTAKBANK.NS", "KIMS.NS", "KWIL.NS", "LTF.NS", "LTTS.NS",
    "LGEINDIA.NS", "LICHSGFIN.NS", "LTFOODS.NS", "LTM.NS", "LT.NS", "LATENTVIEW.NS", "LAURUSLABS.NS", "LXCHEM.NS", "IXIGO.NS",
    "THELEELA.NS", "LEMONTREE.NS", "LENSKART.NS", "LICI.NS", "LINDEINDIA.NS", "LLOYDSENGG.NS", "LLOYDSENT.NS", "LLOYDSME.NS",
    "LODHA.NS", "LUMAXTECH.NS", "LUMAXIND.NS", "LUPIN.NS", "MMTC.NS", "MOIL.NS", "MRF.NS", "MSTCLTD.NS", "MTARTECH.NS", "MBAPL.NS",
    "MGL.NS", "M&MFIN.NS", "M&M.NS", "MANAPPURAM.NS", "MRPL.NS", "MANKIND.NS", "MANORAMA.NS", "MARICO.NS", "MARKSANS.NS", "MARUTI.NS",
    "MASTEK.NS", "MFSL.NS", "MAXHEALTH.NS", "MAZDOCK.NS", "MEDPLUS.NS", "MEESHO.NS", "METROPOLIS.NS", "MINDACORP.NS", "MIDHANI.NS",
    "MSUMI.NS", "MOTILALOFS.NS", "MPHASIS.NS", "BECTORFOOD.NS", "MCX.NS", "MUTHOOTFIN.NS", "NATCOPHARM.NS", "NBCC.NS", "NCC.NS",
    "NEOGEN.NS", "NHPC.NS", "NLCINDIA.NS", "NMDC.NS", "NSLNISP.NS", "NTPCGREEN.NS", "NTPC.NS", "NH.NS", "NATIONALUM.NS", "NFL.NS",
    "NAVA.NS", "NAVINFLUOR.NS", "NAZARA.NS", "NEPHROPLUS.NS", "NESTLEIND.NS", "NETWEB.NS", "NETWORK18.NS", "NEULANDLAB.NS", "NEWGEN.NS",
    "NAM-INDIA.NS", "NIVABUPA.NS", "NORTHARC.NS", "NUVAMA.NS", "NUVOCO.NS", "OBEROIRLTY.NS", "ONGC.NS", "OIL.NS", "OLAELEC.NS",
    "OLECTRA.NS", "OMNI.NS", "KISSHT.NS", "PAYTM.NS", "ONESOURCE.NS", "OFSS.NS", "OSWALPUMPS.NS", "PNGJL.NS", "POLICYBZR.NS",
    "PCJEWELLER.NS", "PCBL.NS", "PDSL.NS", "PGEL.NS", "PIIND.NS", "PNBHOUSING.NS", "PNCINFRA.NS", "PTC.NS", "PTCIL.NS", "PVRINOX.NS",
    "PAGEIND.NS", "PAISALO.NS", "PARADEEP.NS", "PARAS.NS", "PARKHOSPS.NS", "PATANJALI.NS", "PGIL.NS", "PERSISTENT.NS", "PETRONET.NS",
    "PHOENIXLTD.NS", "PWL.NS", "PICCADIL.NS", "PIDILITIND.NS", "PINELABS.NS", "PIRAMALFIN.NS", "PPLPHARMA.NS", "POLYMED.NS", "POLYCAB.NS",
    "POONAWALLA.NS", "PFC.NS", "POWERGRID.NS", "POWERMECH.NS", "POWERICA.NS", "PRAJIND.NS", "PRECWIRE.NS", "PREMIERENE.NS", "PRESTIGE.NS",
    "PRICOLLTD.NS", "PFOCUS.NS", "PRIVISCL.NS", "PGHL.NS", "PNB.NS", "PURVA.NS", "QPOWER.NS", "QUESS.NS", "RRKABEL.NS", "RBLBANK.NS",
    "RECLTD.NS", "RHIM.NS", "RITES.NS", "RADICO.NS", "RVNL.NS", "RAILTEL.NS", "RAIN.NS", "RAINBOW.NS", "RALLIS.NS", "RKFORGE.NS",
    "RCF.NS", "RATEGAIN.NS", "RATNAMANI.NS", "RTNPOWER.NS", "RAYMONDLSL.NS", "REDINGTON.NS", "REFEX.NS", "RELAXO.NS", "RELIANCE.NS",
    "RPOWER.NS", "RELIGARE.NS", "RESPONIND.NS", "RBA.NS", "ROUTE.NS", "RUBICON.NS", "SJS.NS", "SBFC.NS", "SBICARD.NS", "SBILIFE.NS",
    "SEDEMAC.NS", "SGMART.NS", "SIGMAADV.NS", "SJVN.NS", "SKYGOLD.NS", "SMLMAH.NS", "SHRIPISTON.NS", "SRF.NS", "LOTUSDEV.NS", "SAFARI.NS",
    "SAGILITY.NS", "SAILIFE.NS", "SAMHI.NS", "SAMMAANCAP.NS", "MOTHERSON.NS", "SANDUMA.NS", "SANSERA.NS", "SAPPHIRE.NS", "SARDAEN.NS",
    "SAREGAMA.NS", "SCHAEFFLER.NS", "SCHNEIDER.NS", "SENCO.NS", "SENORES.NS", "SHADOWFAX.NS", "SHAILY.NS", "SHAKTIPUMP.NS", "SHARDACROP.NS",
    "SHAREINDIA.NS", "SFL.NS", "SHILCTECH.NS", "SHILPAMED.NS", "SCI.NS", "SHREECEM.NS", "RENUKA.NS", "SHREEJISPG.NS", "SHRIRAMFIN.NS",
    "SHYAMMETL.NS", "ENRIN.NS", "SIEMENS.NS", "SIGNATURE.NS", "SKIPPER.NS", "SOBHA.NS", "SOLARINDS.NS", "SONACOMS.NS", "SONATSOFTW.NS",
    "SOUTHBANK.NS", "STARHEALTH.NS", "SBIN.NS", "SAIL.NS", "SWSOLAR.NS", "STLTECH.NS", "STAR.NS", "STYLAMIND.NS", "SUBROS.NS",
    "SUDARSCHEM.NS", "SUDEEPPHRM.NS", "SUMICHEM.NS", "SPARC.NS", "SUNPHARMA.NS", "SUNTV.NS", "SUNDARMFIN.NS", "SUNDRMFAST.NS",
    "SUNFLAG.NS", "SUNTECK.NS", "SUPREMEIND.NS", "SPLPETRO.NS", "SUPRIYA.NS", "SURYAROSNI.NS", "SUVEN.NS", "SUZLON.NS", "SWANCORP.NS",
    "SWIGGY.NS", "SYNGENE.NS", "SYRMA.NS", "TARC.NS", "TBOTEK.NS", "TDPOWERSYS.NS", "TTKPRESTIG.NS", "TVSMOTOR.NS", "TVSSCS.NS",
    "TMB.NS", "TANLA.NS", "TATACAP.NS", "TATACHEM.NS", "TATACOMM.NS", "TCS.NS", "TATACONSUM.NS", "TATAELXSI.NS", "TATAINVEST.NS",
    "TMCV.NS", "TMPV.NS", "TATAPOWER.NS", "TATASTEEL.NS", "TATATECH.NS", "TTML.NS", "TECHM.NS", "TECHNOE.NS", "TEGA.NS", "TEJASNET.NS",
    "TENNIND.NS", "TEXRAIL.NS", "THANGAMAYL.NS", "NIACL.NS", "RAMCOCEM.NS", "THERMAX.NS", "THOMASCOOK.NS", "THYROCARE.NS", "TI.NS",
    "TIMETECHNO.NS", "TIMEX.NS", "TIMKEN.NS", "TIPSMUSIC.NS", "TITAGARH.NS", "TITAN.NS", "TORNTPHARM.NS", "TORNTPOWER.NS", "TARIL.NS",
    "TRANSRAILL.NS", "TRENT.NS", "TRIDENT.NS", "TRITURBINE.NS", "TIINDIA.NS", "UCOBANK.NS", "UNOMINDA.NS", "UPL.NS", "UTIAMC.NS",
    "UJJIVANSFB.NS", "ULTRACEMCO.NS", "UNIMECH.NS", "UNIONBANK.NS", "UBL.NS", "UNITDSPR.NS", "URBANCO.NS", "USHAMART.NS", "VGUARD.NS",
    "VMART.NS", "VIPIND.NS", "V2RETAIL.NS", "DBREALTY.NS", "WABAG.NS", "VAIBHAVGBL.NS", "VTL.NS", "VBL.NS", "MANYAVAR.NS", "VAML.NS",
    "VISL.NS", "VEDL.NS", "VOGL.NS", "VEDPOWER.NS", "VESUVIUS.NS", "VIJAYA.NS", "VIKRAMSOLR.NS", "VMM.NS", "VIYASH.NS", "IDEA.NS",
    "VOLTAMP.NS", "VOLTAS.NS", "WAAREEENER.NS", "WAAREERTL.NS", "WAKEFIT.NS", "WEWORK.NS", "WEBELSOLAR.NS", "WELCORP.NS", "WELENT.NS",
    "WELSPUNLIV.NS", "WESTLIFE.NS", "WHIRLPOOL.NS", "WIPRO.NS", "WOCKPHARMA.NS", "YATHARTH.NS", "YESBANK.NS", "ZFCVINDIA.NS",
    "ZAGGLE.NS", "ZEEL.NS", "ZENSARTECH.NS", "ZYDUSLIFE.NS", "ZYDUSWELL.NS", "ECLERX.NS"
]

symbols = list(set([s for s in symbols if not s.startswith("DUMMY")]))
print(f"Total symbols to process: {len(symbols)}")

# Download stock metadata in chunks
metadata = {}
chunk_size = 40
for i in range(0, len(symbols), chunk_size):
    chunk = symbols[i:i + chunk_size]
    tickers_obj = yf.Tickers(" ".join(chunk))
    for sym in chunk:
        try:
            info = tickers_obj.tickers[sym].info
            mcap = info.get('marketCap', 0) / 1e7 # convert to Crores (₹ Cr)
            metadata[sym] = {
                "name": info.get('shortName') or info.get('longName') or sym.replace(".NS", ""),
                "industry": info.get('industry') or info.get('sector') or "N/A",
                "marketCapCr": round(mcap, 2) if mcap else 0
            }
        except Exception:
            metadata[sym] = {"name": sym.replace(".NS", ""), "industry": "N/A", "marketCapCr": 0}
    time.sleep(0.3)

# Filter and sort stocks by market cap to assign category dynamically
valid_symbols = [s for s in symbols if metadata[s]["marketCapCr"] > 0]
valid_symbols.sort(key=lambda s: metadata[s]["marketCapCr"], reverse=True)

# Assign Category based on Market Cap Ranking
for rank, sym in enumerate(valid_symbols):
    if rank < 100:
        cat = "Large Cap"
    elif rank < 250:
        cat = "Mid Cap"
    elif rank < 500:
        cat = "Small Cap"
    else:
        cat = "Micro Cap"
    metadata[sym]["category"] = cat

# Fetch Historical Price Data
batch_size = 50
all_data = []
price_dict = {}

for i in range(0, len(valid_symbols), batch_size):
    batch = valid_symbols[i:i + batch_size]
    data = yf.download(batch, period="1y", interval="1d", group_by="ticker", progress=False, threads=True)
    
    for sym in batch:
        try:
            df_stock = data[sym]['Close'].dropna() if len(batch) > 1 else data['Close'].dropna()
            if len(df_stock) < 150:
                continue
            
            clean_sym = sym.replace(".NS", "")
            price_dict[clean_sym] = df_stock

            p_latest = float(df_stock.iloc[-1])
            p_1m = float(df_stock.iloc[-21])
            p_12m = float(df_stock.iloc[0])
            
            r_12m = (p_latest - p_12m) / p_12m
            r_1m = (p_latest - p_1m) / p_1m
            r_adj = r_12m - r_1m
            
            daily_returns = df_stock.pct_change().dropna()
            volatility = float(daily_returns.std() * np.sqrt(252))
            momentum_score = (r_adj / volatility) if volatility > 0 else 0
            
            meta = metadata[sym]
            all_data.append({
                "symbol": clean_sym,
                "name": meta["name"],
                "industry": meta["industry"],
                "marketCapCr": meta["marketCapCr"],
                "category": meta.get("category", "Micro Cap"),
                "price": round(p_latest, 2),
                "return_12m": round(r_12m * 100, 2),
                "volatility": round(volatility * 100, 2),
                "momentum_score": round(momentum_score, 4)
            })
        except Exception:
            continue
    time.sleep(0.3)

with open("data.json", "w") as f:
    json.dump(all_data, f, indent=2)

if price_dict:
    returns_df = pd.DataFrame(price_dict).pct_change().dropna()
    cov_matrix = (returns_df.cov() * 252).round(6)
    with open("cov_matrix.json", "w") as f:
        json.dump(cov_matrix.to_dict(), f)

print("data.json & cov_matrix.json generated successfully!")
