import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title("🎨 Wizzy AI Art Book")

BACKEND_URL = "http://localhost:8000"

# ---------------- SESSION ----------------
if "chat" not in st.session_state:
    st.session_state.chat = []

if "scenes" not in st.session_state:
    st.session_state.scenes = None

# ---------------- CHAT ----------------
st.subheader("💬 Chat with Wizzy")

user_input = st.text_input("Describe your idea")

if st.button("Send"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter something")
    else:
        try:
            res = requests.post(
                f"{BACKEND_URL}/chat/",
                json={"message": user_input},
                timeout=120
            )

            data = res.json()

            if "error" in data:
                st.error("❌ AI Error")
                st.text(data.get("raw", ""))
            else:
                reply = data["reply"]

                st.session_state.chat.append(("You", user_input))
                st.session_state.chat.append(("Wizzy", reply))

                st.session_state.scenes = reply

        except Exception as e:
            st.error(f"❌ Request failed: {e}")

# ---------------- SHOW CHAT ----------------
for role, msg in st.session_state.chat:
    st.write(f"**{role}:** {msg}")

# ---------------- SCENE EDITOR ----------------
st.subheader("🎬 Scene Editor")

if st.session_state.scenes:

    st.markdown(f"### 📖 Title: {st.session_state.scenes.get('title', 'Art Book')}")
    st.markdown(f"🎨 Style: {st.session_state.scenes.get('style', 'cinematic')}")

    scenes = st.session_state.scenes.get("pages", [])

    edited_scenes = []

    for i, scene in enumerate(scenes):
        new_scene = st.text_input(f"Page {i+1}", value=scene, key=f"scene_{i}")
        edited_scenes.append(new_scene)

    st.session_state.scenes["pages"] = edited_scenes

# ---------------- SETTINGS ----------------
st.subheader("⚙️ Settings")

aspect_ratio = st.selectbox(
    "Select Aspect Ratio",
    ["1:1", "3:2", "2:3", "16:9", "9:16"]
)

# ---------------- GENERATE ----------------
st.subheader("🚀 Generate Art Book")

generate_clicked = st.button(
    "Generate Book",
    disabled=st.session_state.scenes is None
)

if generate_clicked:

    scenes = st.session_state.scenes["pages"]
    style = st.session_state.scenes.get("style", "cinematic")
    title = st.session_state.scenes.get("title", "Art Book")

    try:
        with st.spinner("🎨 Generating your art book..."):

            res = requests.post(
                f"{BACKEND_URL}/generate/",
                json={
                    "pages": scenes,
                    "style": style,
                    "aspect_ratio": aspect_ratio,
                    "title": title
                },
                timeout=300   # ✅ increased timeout
            )

        data = res.json()

        # ✅ HANDLE BACKEND ERROR
        if "error" in data:
            st.error("❌ Generation Failed")
            # st.text(data.get("error"))
            # st.text(data.get("details", ""))
            st.stop()

        st.success("✅ Art Book Generated!")

        st.subheader(f"📖 {data.get('title', 'Art Book')}")

        cols = st.columns(2)

        for i, img in enumerate(data["images"]):
            with cols[i % 2]:
                st.image(f"{BACKEND_URL}{img}", use_container_width=True)

        st.subheader("📄 Download")

        pdf_url = f"{BACKEND_URL}{data['pdf']}"
        st.markdown(f"[📥 Download Art Book PDF]({pdf_url})")

    except Exception as e:
        st.error(f"❌ Generation failed: {e}")



#
# import streamlit as st
# import requests
#
# st.set_page_config(layout="wide")
#
# st.title("🎨 Wizzy AI Art Book")
#
# # 🔗 Backend URL
# BACKEND_URL = "http://localhost:8000"
#
# # ---------------- SESSION INIT ----------------
# if "chat" not in st.session_state:
#     st.session_state.chat = []
#
# if "scenes" not in st.session_state:
#     st.session_state.scenes = None
#
# # ---------------- CHAT ----------------
# st.subheader("💬 Chat with Wizzy")
#
# user_input = st.text_input("Describe your idea")
#
# if st.button("Send"):
#
#     if user_input.strip() == "":
#         st.warning("⚠️ Please enter something")
#     else:
#         try:
#             res = requests.post(
#                 f"{BACKEND_URL}/chat/",
#                 json={"message": user_input},
#                 timeout=120
#             )
#
#             data = res.json()
#
#             if "error" in data:
#                 st.error("❌ AI Error")
#                 st.text(data.get("raw", ""))
#             else:
#                 reply = data["reply"]
#
#                 st.session_state.chat.append(("You", user_input))
#                 st.session_state.chat.append(("Wizzy", reply))
#
#                 st.session_state.scenes = reply
#
#         except Exception as e:
#             st.error(f"❌ Request failed: {e}")
#
# # ---------------- SHOW CHAT ----------------
# for role, msg in st.session_state.chat:
#     st.write(f"**{role}:** {msg}")
#
# # ---------------- SCENE EDITOR ----------------
# st.subheader("🎬 Scene Editor")
#
# if st.session_state.scenes:
#
#     st.markdown(f"### 📖 Title: {st.session_state.scenes.get('title', 'Art Book')}")
#     st.markdown(f"🎨 Style: {st.session_state.scenes.get('style', 'cinematic')}")
#
#     scenes = st.session_state.scenes.get("pages", [])
#
#     edited_scenes = []
#
#     for i, scene in enumerate(scenes):
#         new_scene = st.text_input(f"Page {i+1}", value=scene, key=f"scene_{i}")
#         edited_scenes.append(new_scene)
#
#     st.session_state.scenes["pages"] = edited_scenes
#
# # ---------------- SETTINGS ----------------
# st.subheader("⚙️ Settings")
#
# aspect_ratio = st.selectbox(
#     "Select Aspect Ratio",
#     ["3:2", "2:3", "16:9", "9:16"]
# )
#
# # ---------------- GENERATE ----------------
# st.subheader("🚀 Generate Art Book")
#
# generate_clicked = st.button(
#     "Generate Book",
#     disabled=st.session_state.scenes is None
# )
#
# if generate_clicked:
#
#     scenes = st.session_state.scenes["pages"]
#     style = st.session_state.scenes.get("style", "cinematic")
#     title = st.session_state.scenes.get("title", "Art Book")
#
#     try:
#         with st.spinner("🎨 Generating your art book..."):
#
#             res = requests.post(
#                 f"{BACKEND_URL}/generate/",
#                 json={
#                     "pages": scenes,
#                     "style": style,
#                     "aspect_ratio": aspect_ratio,
#                     "title": title
#                 },
#                 timeout=300
#             )
#
#         data = res.json()
#
#         # ---------------- ERROR HANDLING ----------------
#         if "error" in data:
#             st.error("❌ Generation Failed")
#             st.text(data.get("details", data.get("error")))
#             st.stop()
#
#         # ---------------- SUCCESS ----------------
#         st.success("✅ Art Book Generated!")
#
#         st.subheader(f"📖 {data.get('title', 'Art Book')}")
#
#         # ---------------- SHOW IMAGES ----------------
#         cols = st.columns(2)
#
#         for i, img in enumerate(data.get("images", [])):
#             with cols[i % 2]:
#                 st.image(f"{BACKEND_URL}{img}", use_container_width=True)
#
#         # ---------------- DOWNLOAD SECTION ----------------
#         st.subheader("📦 Downloads")
#
#         # PDF Download
#         pdf_url = f"{BACKEND_URL}{data['pdf']}"
#         st.markdown(f"[📥 Download Art Book PDF]({pdf_url})")
#
#         # ZIP Download
#         if "zip" in data:
#             zip_url = f"{BACKEND_URL}{data['zip']}"
#             st.markdown(f"[🗂 Download All Images (ZIP)]({zip_url})")
#
#     except Exception as e:
#         st.error(f"❌ Generation failed: {e}")