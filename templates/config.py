"""
Define substitutions dict here with all defined variables for the templates.
Notes:
    • The value after  # was the standard value.
    • Pixel sizes are related to input resolution.
    • Currently, most <textwidth>-Tags will not be scaled. The factor
      GlobalFontScaling would be a good basis if you want change that.
"""
substitutions = {
    "W": 1280,
    "H": 720,

    # Font scaling is uncoupled from resolution scaling.
    # "GlobalFontScaling": 0.75, # Normal sized font at 720x480
    "GlobalFontScaling": 1.0,  # Big font at 720x480
    # "GlobalFontScaling": 1.1, # Font fits still in most labels.

}


constants = {
    # Values from templates/Includes.xml
    "list_bottom": 0,
    "list_bottom_offset": 80,
    "list_top_offset": 100,
    "list_item_height": 75,
}


# Finally, extend by other dicts here
substitutions.update(constants)
