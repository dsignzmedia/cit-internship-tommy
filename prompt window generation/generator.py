from PIL import Image
import os
import uuid

# ✅ Keyword mappings
frame_keywords = {
    "composite": "frame1.png",
    "french": "frame2.png",
}

handle_keywords = {
    "handle-1": "handle1.png",
    "handle-2": "handle2.png",
    "handle-3": "handle3.png",
    "handle-4": "handle4.png",
    "handle": "handle1.png"
}

panel_keywords = {
    "2-panel pvc": "2-pannel pvc.png",
    "2-panel wooden": "2-pannel wooden.png",
    "3-panel pvc": "3-pannel pvc.png",
    "3-panel wooden": "3-pannel wooden.png",
    "4-panel pvc": "4-pannel pvc.png",
    "4-panel wooden": "4-pannel wooden.png",
}

glass_keywords = {
    "glass-1": "glass1.png",
    "glass-2": "glass2.png",
    "glass-3": "glass3.png"
}

# ✅ Parse user input
def parse_design_elements(text):
    text = text.lower()
    frame = next((frame_keywords[k] for k in frame_keywords if k in text), None)
    panel = next((panel_keywords[k] for k in panel_keywords if k in text), None)
    glass = next((glass_keywords[k] for k in glass_keywords if k in text), None)
    handle = next((handle_keywords[k] for k in handle_keywords if k in text), handle_keywords["handle"])
    return {
        "frame": frame,
        "panel": panel,
        "glass": glass,
        "handle": handle,
        "panel_text": text
    }

# ✅ Manual handle coordinates for 9 specific combinations
manual_handle_coords = {
    ("3-panel wooden", "handle-1"): [(190, 180), (340, 180)],
    ("3-panel wooden", "handle-2"): [(230, 180), (430, 180)],
    ("3-panel wooden", "handle-3"): [(240, 180), (440, 180)],

    ("3-panel pvc", "handle-1"): [(200, 180), (340, 180)],
    ("3-panel pvc", "handle-2"): [(200, 180), (335, 180)],
    ("3-panel pvc", "handle-3"): [(200, 180), (340, 180)],

    ("4-panel pvc", "handle-1"): [(150, 180), (270, 180), (390, 180)],
    ("4-panel pvc", "handle-2"): [(150, 180), (270, 180), (390, 180)],
    ("4-panel pvc", "handle-3"): [(150, 180), (270, 180), (390, 180)],
}

# ✅ Compose final image
def compose_design(images_folder, design_elements):
    base_image = None
    result_image = None
    frame_size = None
    layer_order = ["frame", "glass", "panel"]

    for layer in layer_order:
        file_name = design_elements.get(layer)
        if file_name:
            folder_name = "glass" if layer == "glass" else layer + "s"
            folder_path = os.path.join(images_folder, folder_name)
            img_path = os.path.join(folder_path, file_name)

            if os.path.exists(img_path):
                layer_img = Image.open(img_path).convert("RGBA")

                if base_image is None:
                    frame_size = layer_img.size
                    base_image = Image.new("RGBA", frame_size)
                    result_image = base_image.copy()
                else:
                    layer_img = layer_img.resize(frame_size)

                if layer == "glass" and design_elements.get("panel"):
                    panel_path = os.path.join(images_folder, "panels", design_elements["panel"])
                    if os.path.exists(panel_path):
                        panel_img = Image.open(panel_path).convert("RGBA")
                        panel_img = panel_img.resize(frame_size)
                        mask = panel_img.convert("L").point(lambda p: 255 if p < 200 else 0)
                        layer_img.putalpha(mask)

                base_image = Image.alpha_composite(base_image, layer_img)
                result_image = base_image.copy()

    # ✅ Handle Placement
    handle_file = design_elements.get("handle")
    panel_text = design_elements.get("panel_text", "")
    panel_count = 0
    for i in [2, 3, 4]:
        if f"{i}-panel" in panel_text:
            panel_count = i
            break

    if handle_file and panel_count >= 2:
        handle_path = os.path.join(images_folder, "handles", handle_file)
        if os.path.exists(handle_path):
            handle_img = Image.open(handle_path).convert("RGBA")
            fw, fh = frame_size
            new_w = int(fw * 0.12)
            new_h = int(new_w * (handle_img.height / handle_img.width))
            handle_img = handle_img.resize((new_w, new_h))

            # Determine key
            matched_panel = next((k for k in panel_keywords if k in panel_text), None)
            matched_handle = next((k for k in handle_keywords if handle_keywords[k] == handle_file), "handle")

            key = (matched_panel, matched_handle)

            # Use manual coordinates if available
            if key in manual_handle_coords:
                positions = manual_handle_coords[key]
                for x, y in positions:
                    result_image.paste(handle_img, (x, y), handle_img)
            else:
                # Default: evenly spaced center alignment
                spacing = fw // panel_count
                y_pos = fh // 2 - new_h // 2
                for i in range(1, panel_count):
                    x_pos = spacing * i - new_w // 2
                    result_image.paste(handle_img, (x_pos, y_pos), handle_img)

    return result_image if result_image else None

# ✅ Flask adapter
def chatbot_response(user_text):
    images_folder = "./static/sample_design_images"
    design_elements = parse_design_elements(user_text)
    image = compose_design(images_folder, design_elements)
    return image, None
