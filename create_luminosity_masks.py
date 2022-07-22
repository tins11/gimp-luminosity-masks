#!/usr/bin/python
 
from gimpfu import *
 
def plugin_main(timg, tdrawable):

	# Create copy and desaturate it 
	pdb.gimp_edit_copy(tdrawable) 
	img_BW = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_BW)
	pdb.gimp_item_set_name(img_BW, 'REMOVE') # Could not remove this easily at the end =( 

	pdb.gimp_desaturate_full(img_BW, 1)

	# Highlights: Low (Not so interesting in many cases)
	pdb.gimp_edit_copy(tdrawable) 
	img_HL_L = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_HL_L)
	pdb.gimp_item_set_name(img_HL_L, 'HighLights_Low')

	m_HL_L = pdb.gimp_layer_create_mask(img_HL_L, 5)
	pdb.gimp_layer_add_mask(img_HL_L, m_HL_L) 
	
	# Shadows: High (Not so interesting in many cases)
	pdb.gimp_edit_copy(tdrawable) 
	img_SH_H = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_SH_H)
	pdb.gimp_item_set_name(img_SH_H, 'Shadows_High')

	m_SH_H = pdb.gimp_layer_create_mask(img_SH_H, 0)
	pdb.gimp_channel_combine_masks(m_SH_H, m_HL_L, 1, 0, 0)
	pdb.gimp_layer_add_mask(img_SH_H, m_SH_H) 
		
	# Highlights: High 
	pdb.gimp_edit_copy(tdrawable) 
	img_HL_H = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_HL_H)
	pdb.gimp_item_set_name(img_HL_H, 'Highlights_High')

	m_HL_H = pdb.gimp_layer_create_mask(img_HL_H, 1)
	pdb.gimp_channel_combine_masks(m_HL_H, m_HL_L, 0, 0, 0)
	
	pdb.gimp_channel_combine_masks(m_HL_H, m_SH_H, 1, 0, 0)
	pdb.gimp_layer_add_mask(img_HL_H, m_HL_H) 
	
	# Shadows: Low 
	pdb.gimp_edit_copy(tdrawable) 
	img_SH_L = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_SH_L)
	pdb.gimp_item_set_name(img_SH_L, 'Shadows_Low')

	m_SH_L = pdb.gimp_layer_create_mask(img_SH_L, 1)
	pdb.gimp_channel_combine_masks(m_SH_L, m_SH_H, 0, 0, 0)
	
	pdb.gimp_channel_combine_masks(m_SH_L, m_HL_L, 1, 0, 0)
	pdb.gimp_layer_add_mask(img_SH_L, m_SH_L) 
	
	# Midtones: Mid 
	pdb.gimp_edit_copy(tdrawable) 
	img_MT = pdb.gimp_edit_paste(tdrawable, 1)
	pdb.gimp_floating_sel_to_layer(img_MT)
	pdb.gimp_item_set_name(img_MT, 'Mid_tones')

	m_MT = pdb.gimp_layer_create_mask(img_MT, 1)
	pdb.gimp_channel_combine_masks(m_MT, m_HL_L, 0, 0, 0)
	
	pdb.gimp_channel_combine_masks(m_MT, m_SH_H, 3, 0, 0)
	pdb.gimp_layer_add_mask(img_MT, m_MT) 
  
	# Set not-so-interesting layers to be invisible 
	pdb.gimp_item_set_visible(img_BW, 0)
	pdb.gimp_item_set_visible(img_HL_L, 0)
	pdb.gimp_item_set_visible(img_SH_H, 0)
 
 
register(
        "python_fu_create_luminosity_masks",
        "Creates five luminosity masks: (1) Highlights high, (2) Highlights low, (3) Mid tones, (4) Shadows high and (5) Shadows low.",
        "Creates luminosity masks",
        "tins11",
        "tins11",
        "2017",
        "<Image>/Colors/Auto/Luminosity masks...",
        "RGB*",
        [],
        [],
        plugin_main)
 
main()