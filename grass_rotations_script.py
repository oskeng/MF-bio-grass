#!/usr/bin/python3.10
#
# Strategic perennialization: grass rotations
#
# Author: Oskar Englund
# Email: oskar.englund@gmail.com
#
######################

import sys
import grass.script as gscript
import time
from grass.pygrass.modules import Module
from grass.pygrass.modules.shortcuts import general as g
from grass.pygrass.modules.shortcuts import vector as v
from colorama import Fore
from tkinter import *      
import tkinter.messagebox
import time
from datetime import datetime

########################
#
# Modeling functions
#
########################


def get_time():
    now = datetime.now()
    return now.strftime("%H:%M:%S")


print(Fore.CYAN + "\n Model initiated... \n Current time:", get_time(), "\n")
print(Fore.WHITE)

vectinmap = 'MF2_grass_rotations_input'
vectoutmap = 'MF2_grass_rotations_output'
vectoutmap_suitable = "MF2_grass_rotations_output_suitable"
export_path_gpkg = "/home/oskeng/Dropbox/Jobb/Chalmers/Projekt/Aktuellt/ES-papper/MF_bio/Paper_2/GIS/mf2.gpkg"
export_path_calculations = "/home/oskeng/Dropbox/Jobb/Chalmers/Projekt/Aktuellt/ES-papper/MF_bio/Paper_2/GIS/Calculations/Scripts/Grass rotations/"


def start_over():

    g.copy(vector=(vectinmap,vectoutmap),overwrite=True)

    
def get_data():
    
    """
    avg_grass_med created manually using:
    v.db.join --verbose map=MF2_grass_rotations_output@MF-bio column=NUTS3 
    other_table=yields_selected other_column=NUTS_ID subset_columns=avg_grass_med
    
    Simulated SOC values by 2020, 2050, and 2100 from 2y ley systems 
    calculated manually by rasterizing JRC data and running v.rast.stats.
    (AR_LEY_year)
    
    Simulated SOC values by 2020, 2050, and 2100 from permanent grasslands
    calculated manually by rasterizing JRC data and running v.rast.stats.
    (AR_GR_LUC_year)
    
    Simulated baseline SOC values by 2020, 2050, and 2100 calculfrom grass.pygrass.modules.shortcuts import general as gated manually 
    by rasterizing JRC data and running v.rast.stats.
    (bl_year)
    
    See log for details. 
    """
         
    
def scenarios():
    start_time = time.time()
    
    Module("v.db.addcolumn",
    map=vectoutmap,
    columns="low_est_system,high_est_system,\
            low_est_area_factor double precision,high_est_area_factor double precision,\
            low_est_biomass_factor double precision,high_est_biomass_factor double precision,\
            low_est_SOCinc_factor double precision,high_est_SOCinc_factor double precision")

### system
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_system",
    value="2y_lim25",
    where="SOC_sat_cap=2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_system",
    value="2y_lim50",
    where="SOC_sat_cap=3")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_system",
    value="2y",
    where="SOC_sat_cap=4")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_system",
    value="2y",
    where="SOC_sat_cap=2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_system",
    value="3y",
    where="SOC_sat_cap=3")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_system",
    value="4y",
    where="SOC_sat_cap=4")
    
#### area factor
    area_factor_2y = 0.3333333 #1/3
    area_factor_2y_lim50 = 0.1666666 #(1/3)/2
    area_factor_2y_lim25 = 0.0833333 #(1/3)/4
    area_factor_3y = 0.428571 #3/7
    area_factor_4y = 0.5 #1/2
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_area_factor",
    value=area_factor_2y_lim25,
    where="low_est_system='2y_lim25'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_area_factor",
    value=area_factor_2y_lim50,
    where="low_est_system='2y_lim50'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_area_factor",
    value=area_factor_2y,
    where="low_est_system='2y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_area_factor",
    value=area_factor_2y,
    where="high_est_system='2y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_area_factor",
    value=area_factor_3y,
    where="high_est_system='3y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_area_factor",
    value=area_factor_4y,
    where="high_est_system='4y'")
    
#### biomass factor
    biomass_factor_2y = 0.75 # 3/4
    biomass_factor_3y = 0.8333333 #5/6
    biomass_factor_4y = 0.875 #7/8
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_biomass_factor",
    value=biomass_factor_2y,
    where="low_est_system is not null")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_biomass_factor",
    value=biomass_factor_2y,
    where="high_est_system='2y'")

    Module("v.db.update",
    map=vectoutmap,
    column="high_est_biomass_factor",
    value=biomass_factor_3y,
    where="high_est_system='3y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_biomass_factor",
    value=biomass_factor_4y,
    where="high_est_system='4y'")
    
#### SOCinc factor

    SOCinc_factor_2y_lim25 = 0.25 #1/4
    SOCinc_factor_2y_lim50 = 0.5 #1/2
    SOCinc_factor_2y = 1
    SOCinc_factor_3y = 1.2857 #9/7
    SOCinc_factor_4y = 1.5 #3/2


    Module("v.db.update",
    map=vectoutmap,
    column="low_est_SOCinc_factor",
    value=SOCinc_factor_2y_lim25,
    where="low_est_system='2y_lim25'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_SOCinc_factor",
    value=SOCinc_factor_2y_lim50,
    where="low_est_system='2y_lim50'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_SOCinc_factor",
    value=SOCinc_factor_2y,
    where="low_est_system='2y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_SOCinc_factor",
    value=SOCinc_factor_2y,
    where="high_est_system='2y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_SOCinc_factor",
    value=SOCinc_factor_3y,
    where="high_est_system='3y'")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_SOCinc_factor",
    value=SOCinc_factor_4y,
    where="high_est_system='4y'")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n scenarios() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print('\a')
    print(Fore.WHITE)
    
    
def area():
    start_time = time.time()

# Calculate average area for the different systems

    start_time = time.time()

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="area_2y int,area_2y_lim50 int,area_2y_lim25 int,area_3y int,area_4y int")
    
    Module("v.db.update",
    map=vectoutmap,
    column="area_2y",
    query_column="annual_crops_number/3")   

    Module("v.db.update",
    map=vectoutmap,
    column="area_2y_lim50",
    query_column="area_2y/2")

    Module("v.db.update",
    map=vectoutmap,
    column="area_2y_lim25",
    query_column="area_2y/4")

    Module("v.db.update",
    map=vectoutmap,
    column="area_3y",
    query_column="annual_crops_number*3/7")

    Module("v.db.update",
    map=vectoutmap,
    column="area_4y",
    query_column="annual_crops_number*0.5")
    
    # scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="low_est_area int,high_est_area int")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_area",
    query_column="annual_crops_number*low_est_area_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_area",
    query_column="annual_crops_number*high_est_area_factor")
    
    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n area() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def biomass():
    start_time = time.time()

    """
    Calculate biomass production per ha and year from the different systems.
    """
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="biomass_2y int,biomass_2y_lim50 int,biomass_2y_lim25 int,biomass_3y int,biomass_4y int")
    
    Module("v.db.update",
    map=vectoutmap,
    column="biomass_2y",
    query_column="area_2y*avg_grass_med*3/4")
    
    Module("v.db.update",
    map=vectoutmap,
    column="biomass_2y_lim50",
    query_column="area_2y_lim50*avg_grass_med*3/4")

    Module("v.db.update",
    map=vectoutmap,
    column="biomass_2y_lim25",
    query_column="area_2y_lim25*avg_grass_med*3/4")

    Module("v.db.update",
    map=vectoutmap,
    column="biomass_3y",
    query_column="area_3y*avg_grass_med *5/6")

    Module("v.db.update",
    map=vectoutmap,
    column="biomass_4y",
    query_column="area_4y*avg_grass_med*7/8")

# scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="low_est_biomass int,high_est_biomass int")
    
    Module("v.db.update",
    map=vectoutmap,
    column="low_est_biomass",
    query_column="low_est_area*avg_grass_med*low_est_biomass_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="high_est_biomass",
    query_column="high_est_area*avg_grass_med*high_est_biomass_factor")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n biomass() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
    
def SOC_increase_relative_BAU():
    start_time = time.time()
    
# Calculating SOC increase relative BAU, in 2050 and 2100

#### per hectare
    """
    SOC increase (t C/ha)
    
    Since SOCinc values use base year 2010, they need to be recalculated to base year 2020. See methods.
    For explanation of SOCinc calc for other than default (2y), see methods. 
    """

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perha_2y_2050 double precision,SOCinc_BAU_perha_2y_lim50_2050 double precision,\
    SOCinc_BAU_perha_2y_lim25_2050 double precision,SOCinc_BAU_perha_3y_2050 double precision,\
    SOCinc_BAU_perha_4y_2050 double precision,SOCinc_BAU_perha_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perha_2y_2080 double precision,SOCinc_BAU_perha_2y_lim50_2080 double precision,\
    SOCinc_BAU_perha_2y_lim25_2080 double precision,SOCinc_BAU_perha_3y_2080 double precision,\
    SOCinc_BAU_perha_4y_2080 double precision,SOCinc_BAU_perha_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perha_2y_2100 double precision,SOCinc_BAU_perha_2y_lim50_2100 double precision,\
    SOCinc_BAU_perha_2y_lim25_2100 double precision,SOCinc_BAU_perha_3y_2100 double precision,\
    SOCinc_BAU_perha_4y_2100 double precision,SOCinc_BAU_perha_permgrass_2100 double precision")
    
    Module("v.db.update", 
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_2050",
    query_column="AR_LEY_y2020 + (AR_LEY_y2050 - AR_LEY_y2020)*2/3")

    Module("v.db.update", 
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_2080",
    query_column="AR_LEY_y2020 + (AR_LEY_y2080 - AR_LEY_y2020)*5/6")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_2100",
    query_column="AR_LEY_y2020 + (AR_LEY_y2100 - AR_LEY_y2020)*7/8")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim50_2050",
    query_column="SOCinc_BAU_perha_2y_2050/2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim50_2080",
    query_column="SOCinc_BAU_perha_2y_2080/2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim50_2100",
    query_column="SOCinc_BAU_perha_2y_2100/2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim25_2050",
    query_column="SOCinc_BAU_perha_2y_2050/4")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim25_2080",
    query_column="SOCinc_BAU_perha_2y_2080/4")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_2y_lim25_2100",
    query_column="SOCinc_BAU_perha_2y_2100/4")
            
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_3y_2050",
    query_column="SOCinc_BAU_perha_2y_2050*9/7")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_3y_2080",
    query_column="SOCinc_BAU_perha_2y_2080*9/7")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_3y_2100",
    query_column="SOCinc_BAU_perha_2y_2100*9/7")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_4y_2050",
    query_column="SOCinc_BAU_perha_2y_2050*3/2")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_4y_2080",
    query_column="SOCinc_BAU_perha_2y_2080*3/2")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_4y_2100",
    query_column="SOCinc_BAU_perha_2y_2100*3/2")
    
    Module("v.db.update", 
    map=vectoutmap,
    column="SOCinc_BAU_perha_permgrass_2050",
    query_column="AR_GR_LUC_y2020 + (AR_GR_LUC_y2050 - AR_GR_LUC_y2020)*2/3")

    Module("v.db.update", 
    map=vectoutmap,
    column="SOCinc_BAU_perha_permgrass_2080",
    query_column="AR_GR_LUC_y2020 + (AR_GR_LUC_y2080 - AR_GR_LUC_y2020)*5/6")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_permgrass_2100",
    query_column="AR_GR_LUC_y2020 + (AR_GR_LUC_y2100 - AR_GR_LUC_y2020)*7/8")
    
    # scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perha_low_est_2050 double precision,SOCinc_BAU_perha_low_est_2080 double precision,SOCinc_BAU_perha_low_est_2100 double precision,\
            SOCinc_BAU_perha_high_est_2050 double precision,SOCinc_BAU_perha_high_est_2080 double precision,SOCinc_BAU_perha_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_low_est_2050",
    query_column="SOCinc_BAU_perha_2y_2050*low_est_SOCinc_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_low_est_2080",
    query_column="SOCinc_BAU_perha_2y_2080*low_est_SOCinc_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_low_est_2100",
    query_column="SOCinc_BAU_perha_2y_2100*low_est_SOCinc_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_high_est_2050",
    query_column="SOCinc_BAU_perha_2y_2050*high_est_SOCinc_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_high_est_2080",
    query_column="SOCinc_BAU_perha_2y_2080*high_est_SOCinc_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perha_high_est_2100",
    query_column="SOCinc_BAU_perha_2y_2100*high_est_SOCinc_factor")
    
#### total SOC increase (t C) ####

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_total_2y_2050 double precision,SOCinc_BAU_total_2y_lim50_2050 double precision,\
    SOCinc_BAU_total_2y_lim25_2050 double precision,SOCinc_BAU_total_3y_2050 double precision,\
    SOCinc_BAU_total_4y_2050 double precision,SOCinc_BAU_total_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_total_2y_2080 double precision,SOCinc_BAU_total_2y_lim50_2080 double precision,\
    SOCinc_BAU_total_2y_lim25_2080 double precision,SOCinc_BAU_total_3y_2080 double precision,\
    SOCinc_BAU_total_4y_2080 double precision,SOCinc_BAU_total_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_total_2y_2100 double precision,SOCinc_BAU_total_2y_lim50_2100 double precision,\
    SOCinc_BAU_total_2y_lim25_2100 double precision,SOCinc_BAU_total_3y_2100 double precision,\
    SOCinc_BAU_total_4y_2100 double precision,SOCinc_BAU_total_permgrass_2100 double precision")
  
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_2050",
    query_column="SOCinc_BAU_perha_2y_2050*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_2080",
    query_column="SOCinc_BAU_perha_2y_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_2100",
    query_column="SOCinc_BAU_perha_2y_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim50_2050",
    query_column="SOCinc_BAU_perha_2y_lim50_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim50_2080",
    query_column="SOCinc_BAU_perha_2y_lim50_2080*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim50_2100",
    query_column="SOCinc_BAU_perha_2y_lim50_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim25_2050",
    query_column="SOCinc_BAU_perha_2y_lim25_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim25_2080",
    query_column="SOCinc_BAU_perha_2y_lim25_2080*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_2y_lim25_2100",
    query_column="SOCinc_BAU_perha_2y_lim25_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_3y_2050",
    query_column="SOCinc_BAU_perha_3y_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_3y_2080",
    query_column="SOCinc_BAU_perha_3y_2080*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_3y_2100",
    query_column="SOCinc_BAU_perha_3y_2100*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_4y_2050",
    query_column="SOCinc_BAU_perha_4y_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_4y_2080",
    query_column="SOCinc_BAU_perha_4y_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_4y_2100",
    query_column="SOCinc_BAU_perha_4y_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_permgrass_2050",
    query_column="SOCinc_BAU_perha_permgrass_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_permgrass_2080",
    query_column="SOCinc_BAU_perha_permgrass_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_permgrass_2100",
    query_column="SOCinc_BAU_perha_permgrass_2100*annual_crops_number")

    # scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_total_low_est_2050 double precision,SOCinc_BAU_total_low_est_2080 double precision,SOCinc_BAU_total_low_est_2100 double precision,\
            SOCinc_BAU_total_high_est_2050 double precision,SOCinc_BAU_total_high_est_2080 double precision,SOCinc_BAU_total_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_low_est_2050",
    query_column="SOCinc_BAU_perha_low_est_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_low_est_2080",
    query_column="SOCinc_BAU_perha_low_est_2080*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_low_est_2100",
    query_column="SOCinc_BAU_perha_low_est_2100*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_high_est_2050",
    query_column="SOCinc_BAU_perha_high_est_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_high_est_2080",
    query_column="SOCinc_BAU_perha_high_est_2080*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_total_high_est_2100",
    query_column="SOCinc_BAU_perha_high_est_2100*annual_crops_number")

#### SOC increase relative BAU (%) ####

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perc_2y_2050 double precision,SOCinc_BAU_perc_2y_lim50_2050 double precision,\
    SOCinc_BAU_perc_2y_lim25_2050 double precision,SOCinc_BAU_perc_3y_2050 double precision,\
    SOCinc_BAU_perc_4y_2050 double precision,SOCinc_BAU_perc_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perc_2y_2080 double precision,SOCinc_BAU_perc_2y_lim50_2080 double precision,\
    SOCinc_BAU_perc_2y_lim25_2080 double precision,SOCinc_BAU_perc_3y_2080 double precision,\
    SOCinc_BAU_perc_4y_2080 double precision,SOCinc_BAU_perc_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perc_2y_2100 double precision,SOCinc_BAU_perc_2y_lim50_2100 double precision,\
    SOCinc_BAU_perc_2y_lim25_2100 double precision,SOCinc_BAU_perc_3y_2100 double precision,\
    SOCinc_BAU_perc_4y_2100 double precision,SOCinc_BAU_perc_permgrass_2100 double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_2y_2050)/bl_y2050)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_2y_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_2y_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim50_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_2y_lim50_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim50_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_2y_lim50_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim50_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_2y_lim50_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim25_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_2y_lim25_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim25_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_2y_lim25_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_2y_lim25_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_2y_lim25_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_3y_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_3y_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_3y_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_3y_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_3y_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_3y_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_4y_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_4y_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_4y_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_4y_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_4y_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_4y_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_permgrass_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_permgrass_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_permgrass_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_permgrass_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_permgrass_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_permgrass_2100)/bl_y2100)-1")
    
    # scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_BAU_perc_low_est_2050 double precision,SOCinc_BAU_perc_low_est_2080 double precision,SOCinc_BAU_perc_low_est_2100 double precision,\
            SOCinc_BAU_perc_high_est_2050 double precision,SOCinc_BAU_perc_high_est_2080 double precision,SOCinc_BAU_perc_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_low_est_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_low_est_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_low_est_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_low_est_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_low_est_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_low_est_2100)/bl_y2100)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_high_est_2050",
    query_column="((bl_y2050+SOCinc_BAU_perha_high_est_2050)/bl_y2050)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_high_est_2080",
    query_column="((bl_y2080+SOCinc_BAU_perha_high_est_2080)/bl_y2080)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_BAU_perc_high_est_2100",
    query_column="((bl_y2100+SOCinc_BAU_perha_high_est_2100)/bl_y2100)-1")
        
    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n SOC_increase_relative_BAU() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def SOC_increase_relative_2020():
    start_time = time.time()

# Calculating SOC values relative 2020 level, in 2050 and 2100

#### per hectare
   
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perha_2y_2050 double precision,SOCinc_2020_perha_2y_lim50_2050 double precision,\
    SOCinc_2020_perha_2y_lim25_2050 double precision,SOCinc_2020_perha_3y_2050 double precision,\
    SOCinc_2020_perha_4y_2050 double precision,SOCinc_2020_perha_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perha_2y_2080 double precision,SOCinc_2020_perha_2y_lim50_2080 double precision,\
    SOCinc_2020_perha_2y_lim25_2080 double precision,SOCinc_2020_perha_3y_2080 double precision,\
    SOCinc_2020_perha_4y_2080 double precision,SOCinc_2020_perha_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perha_2y_2100 double precision,SOCinc_2020_perha_2y_lim50_2100 double precision,\
    SOCinc_2020_perha_2y_lim25_2100 double precision,SOCinc_2020_perha_3y_2100 double precision,\
    SOCinc_2020_perha_4y_2100 double precision,SOCinc_2020_perha_permgrass_2100 double precision")
    
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_2050",
    query_column="SOCinc_BAU_perha_2y_2050+(bl_y2050-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_2080",
    query_column="SOCinc_BAU_perha_2y_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_2100",
    query_column="SOCinc_BAU_perha_2y_2100+(bl_y2100-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim50_2050",
    query_column="SOCinc_BAU_perha_2y_lim50_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim50_2080",
    query_column="SOCinc_BAU_perha_2y_lim50_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim50_2100",
    query_column="SOCinc_BAU_perha_2y_lim50_2100+(bl_y2100-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim25_2050",
    query_column="SOCinc_BAU_perha_2y_lim25_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim25_2080",
    query_column="SOCinc_BAU_perha_2y_lim25_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_2y_lim25_2100",
    query_column="SOCinc_BAU_perha_2y_lim25_2100+(bl_y2100-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_3y_2050",
    query_column="SOCinc_BAU_perha_3y_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_3y_2080",
    query_column="SOCinc_BAU_perha_3y_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_3y_2100",
    query_column="SOCinc_BAU_perha_3y_2100+(bl_y2100-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_4y_2050",
    query_column="SOCinc_BAU_perha_4y_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_4y_2080",
    query_column="SOCinc_BAU_perha_4y_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_4y_2100",
    query_column="SOCinc_BAU_perha_4y_2100+(bl_y2100-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_permgrass_2050",
    query_column="SOCinc_BAU_perha_permgrass_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_permgrass_2080",
    query_column="SOCinc_BAU_perha_permgrass_2080+(bl_y2080-bl_y2020)")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_permgrass_2100",
    query_column="SOCinc_BAU_perha_permgrass_2100+(bl_y2100-bl_y2020)")

# Scenarios
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perha_low_est_2050 double precision,SOCinc_2020_perha_low_est_2080 double precision,SOCinc_2020_perha_low_est_2100 double precision,\
            SOCinc_2020_perha_high_est_2050 double precision,SOCinc_2020_perha_high_est_2080 double precision,SOCinc_2020_perha_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_low_est_2050",
    query_column="SOCinc_BAU_perha_low_est_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_low_est_2080",
    query_column="SOCinc_BAU_perha_low_est_2080+(bl_y2080-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_low_est_2100",
    query_column="SOCinc_BAU_perha_low_est_2100+(bl_y2100-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_high_est_2050",
    query_column="SOCinc_BAU_perha_high_est_2050+(bl_y2050-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_high_est_2080",
    query_column="SOCinc_BAU_perha_high_est_2080+(bl_y2080-bl_y2020)")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perha_high_est_2100",
    query_column="SOCinc_BAU_perha_high_est_2100+(bl_y2100-bl_y2020)")
    
#### total

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_total_2y_2050 double precision,SOCinc_2020_total_2y_lim50_2050 double precision,\
    SOCinc_2020_total_2y_lim25_2050 double precision,SOCinc_2020_total_3y_2050 double precision,\
    SOCinc_2020_total_4y_2050 double precision,SOCinc_2020_total_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_total_2y_2080 double precision,SOCinc_2020_total_2y_lim50_2080 double precision,\
    SOCinc_2020_total_2y_lim25_2080 double precision,SOCinc_2020_total_3y_2080 double precision,\
    SOCinc_2020_total_4y_2080 double precision,SOCinc_2020_total_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_total_2y_2100 double precision,SOCinc_2020_total_2y_lim50_2100 double precision,\
    SOCinc_2020_total_2y_lim25_2100 double precision,SOCinc_2020_total_3y_2100 double precision,\
    SOCinc_2020_total_4y_2100 double precision,SOCinc_2020_total_permgrass_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_2050",
    query_column="SOCinc_2020_perha_2y_2050*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_2080",
    query_column="SOCinc_2020_perha_2y_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_2100",
    query_column="SOCinc_2020_perha_2y_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim50_2050",
    query_column="SOCinc_2020_perha_2y_lim50_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim50_2080",
    query_column="SOCinc_2020_perha_2y_lim50_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim50_2100",
    query_column="SOCinc_2020_perha_2y_lim50_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim25_2050",
    query_column="SOCinc_2020_perha_2y_lim25_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim25_2080",
    query_column="SOCinc_2020_perha_2y_lim25_2080*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_2y_lim25_2100",
    query_column="SOCinc_2020_perha_2y_lim25_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_3y_2050",
    query_column="SOCinc_2020_perha_3y_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_3y_2080",
    query_column="SOCinc_2020_perha_3y_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_3y_2100",
    query_column="SOCinc_2020_perha_3y_2100*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_4y_2050",
    query_column="SOCinc_2020_perha_4y_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_4y_2080",
    query_column="SOCinc_2020_perha_4y_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_4y_2100",
    query_column="SOCinc_2020_perha_4y_2100*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_permgrass_2050",
    query_column="SOCinc_2020_perha_permgrass_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_permgrass_2080",
    query_column="SOCinc_2020_perha_permgrass_2080*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_permgrass_2100",
    query_column="SOCinc_2020_perha_permgrass_2100*annual_crops_number")
    
# Scenarios

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_total_low_est_2050 double precision,SOCinc_2020_total_low_est_2080 double precision,SOCinc_2020_total_low_est_2100 double precision,\
            SOCinc_2020_total_high_est_2050 double precision,SOCinc_2020_total_high_est_2080 double precision,SOCinc_2020_total_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_low_est_2050",
    query_column="SOCinc_2020_perha_low_est_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_low_est_2080",
    query_column="SOCinc_2020_perha_low_est_2080*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_low_est_2100",
    query_column="SOCinc_2020_perha_low_est_2100*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_high_est_2050",
    query_column="SOCinc_2020_perha_high_est_2050*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_high_est_2080",
    query_column="SOCinc_2020_perha_high_est_2080*annual_crops_number")
        
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_total_high_est_2100",
    query_column="SOCinc_2020_perha_high_est_2100*annual_crops_number")
    
#### %

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perc_2y_2050 double precision,SOCinc_2020_perc_2y_lim50_2050 double precision,\
    SOCinc_2020_perc_2y_lim25_2050 double precision,SOCinc_2020_perc_3y_2050 double precision,\
    SOCinc_2020_perc_4y_2050 double precision,SOCinc_2020_perc_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perc_2y_2080 double precision,SOCinc_2020_perc_2y_lim50_2080 double precision,\
    SOCinc_2020_perc_2y_lim25_2080 double precision,SOCinc_2020_perc_3y_2080 double precision,\
    SOCinc_2020_perc_4y_2080 double precision,SOCinc_2020_perc_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perc_2y_2100 double precision,SOCinc_2020_perc_2y_lim50_2100 double precision,\
    SOCinc_2020_perc_2y_lim25_2100 double precision,SOCinc_2020_perc_3y_2100 double precision,\
    SOCinc_2020_perc_4y_2100 double precision,SOCinc_2020_perc_permgrass_2100 double precision")
        
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_2050)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_2100)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim50_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim50_2050)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim50_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim50_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim50_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim50_2100)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim25_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim25_2050)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim25_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim25_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_2y_lim25_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_2y_lim25_2100)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_3y_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_3y_2050)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_3y_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_3y_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_3y_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_3y_2100)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_4y_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_4y_2050)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_4y_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_4y_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_4y_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_4y_2100)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_permgrass_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_permgrass_2050)/bl_y2020)-1")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_permgrass_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_permgrass_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_permgrass_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_permgrass_2100)/bl_y2020)-1")
    
# Scenarios

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOCinc_2020_perc_low_est_2050 double precision,SOCinc_2020_perc_low_est_2080 double precision,SOCinc_2020_perc_low_est_2100 double precision,\
            SOCinc_2020_perc_high_est_2050 double precision,SOCinc_2020_perc_high_est_2080 double precision,SOCinc_2020_perc_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_low_est_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_low_est_2050)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_low_est_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_low_est_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_low_est_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_low_est_2100)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_high_est_2050",
    query_column="((bl_y2020+SOCinc_2020_perha_high_est_2050)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_high_est_2080",
    query_column="((bl_y2020+SOCinc_2020_perha_high_est_2080)/bl_y2020)-1")

    Module("v.db.update",
    map=vectoutmap,
    column="SOCinc_2020_perc_high_est_2100",
    query_column="((bl_y2020+SOCinc_2020_perha_high_est_2100)/bl_y2020)-1")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n SOC_increase_relative_2020() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def SOC_values_perha():
    start_time = time.time()

    """    
    Calculate new SOC values per ha in 2050 and 2100 for the different ley systems and for permanent grassland.
    For ley, adding SOC increases relative 2020 to baseline SOC in 2020
    For permgrass, SOC increases are downscaled due to different starting year 
    
    """

    # baseline
    
    """
    bl_y[year] = BAU SOC in t C/ha in [year]
    """
    
    # Ley systems per ha
          
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOC_2y_2050 double precision,SOC_2y_lim50_2050 double precision,\
    SOC_2y_lim25_2050 double precision,SOC_3y_2050 double precision,\
    SOC_4y_2050 double precision,SOC_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOC_2y_2080 double precision,SOC_2y_lim50_2080 double precision,\
    SOC_2y_lim25_2080 double precision,SOC_3y_2080 double precision,\
    SOC_4y_2080 double precision,SOC_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOC_2y_2100 double precision,SOC_2y_lim50_2100 double precision,\
    SOC_2y_lim25_2100 double precision,SOC_3y_2100 double precision,\
    SOC_4y_2100 double precision,SOC_permgrass_2100 double precision")  
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_2050",
    query_column="SOCinc_2020_perha_2y_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_2080",
    query_column="SOCinc_2020_perha_2y_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_2100",
    query_column="SOCinc_2020_perha_2y_2100 + bl_y2100")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim50_2050",
    query_column="SOCinc_2020_perha_2y_lim50_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim50_2080",
    query_column="SOCinc_2020_perha_2y_lim50_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim50_2100",
    query_column="SOCinc_2020_perha_2y_lim50_2100 + bl_y2020")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim25_2050",
    query_column="SOCinc_2020_perha_2y_lim25_2050 + bl_y2020")
           
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim25_2080",
    query_column="SOCinc_2020_perha_2y_lim25_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_2y_lim25_2100",
    query_column="SOCinc_2020_perha_2y_lim25_2100 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_3y_2050",
    query_column="SOCinc_2020_perha_3y_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_3y_2080",
    query_column="SOCinc_2020_perha_3y_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_3y_2100",
    query_column="SOCinc_2020_perha_3y_2100 + bl_y2020")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_4y_2050",
    query_column="SOCinc_2020_perha_4y_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_4y_2080",
    query_column="SOCinc_2020_perha_4y_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_4y_2100",
    query_column="SOCinc_2020_perha_4y_2100 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_permgrass_2050",
    query_column="SOCinc_2020_perha_permgrass_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_permgrass_2080",
    query_column="SOCinc_2020_perha_permgrass_2080 + bl_y2020")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_permgrass_2100",
    query_column="SOCinc_2020_perha_permgrass_2100 + bl_y2020")
    
# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="SOC_low_est_2050 double precision,SOC_low_est_2080 double precision,SOC_low_est_2100 double precision,\
            SOC_high_est_2050 double precision,SOC_high_est_2080 double precision,SOC_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_low_est_2050",
    query_column="SOCinc_2020_perha_low_est_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_low_est_2080",
    query_column="SOCinc_2020_perha_low_est_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_low_est_2100",
    query_column="SOCinc_2020_perha_low_est_2100 + bl_y2020")
    
    Module("v.db.update",
    map=vectoutmap,
    column="SOC_high_est_2050",
    query_column="SOCinc_2020_perha_high_est_2050 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_high_est_2080",
    query_column="SOCinc_2020_perha_high_est_2080 + bl_y2020")

    Module("v.db.update",
    map=vectoutmap,
    column="SOC_high_est_2100",
    query_column="SOCinc_2020_perha_high_est_2100 + bl_y2020")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n SOC_values_perha() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)

def comp_max_SOCinc(): 
    start_time = time.time()

    """
    Here, we calculate how large share of the maximum SOC increase (i.e., from permgrass)
    that can be achieved by the ley systems.
    
    This can also be interpreted as the share of annual crop area that needs to be 
    converted to permgrass to achieve the same SOC increases as the ley systems.
    
    """

    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="comp_max_SOCinc_2y_2050 double precision,comp_max_SOCinc_2y_lim50_2050 double precision,\
    comp_max_SOCinc_2y_lim25_2050 double precision,comp_max_SOCinc_3y_2050 double precision,\
    comp_max_SOCinc_4y_2050 double precision,comp_max_SOCinc_permgrass_2050 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="comp_max_SOCinc_2y_2080 double precision,comp_max_SOCinc_2y_lim50_2080 double precision,\
    comp_max_SOCinc_2y_lim25_2080 double precision,comp_max_SOCinc_3y_2080 double precision,\
    comp_max_SOCinc_4y_2080 double precision,comp_max_SOCinc_permgrass_2080 double precision")
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="comp_max_SOCinc_2y_2100 double precision,comp_max_SOCinc_2y_lim50_2100 double precision,\
    comp_max_SOCinc_2y_lim25_2100 double precision,comp_max_SOCinc_3y_2100 double precision,\
    comp_max_SOCinc_4y_2100 double precision,comp_max_SOCinc_permgrass_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_2050",
    query_column="SOCinc_2020_perha_2y_2050/SOCinc_2020_perha_permgrass_2050")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_2080",
    query_column="SOCinc_2020_perha_2y_2080/SOCinc_2020_perha_permgrass_2080")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_2100",
    query_column="SOCinc_2020_perha_2y_2100/SOCinc_2020_perha_permgrass_2100")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim50_2050",
    query_column="SOCinc_2020_perha_2y_lim50_2050/SOCinc_2020_perha_permgrass_2050")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim50_2080",
    query_column="SOCinc_2020_perha_2y_lim50_2080/SOCinc_2020_perha_permgrass_2080")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim50_2100",
    query_column="SOCinc_2020_perha_2y_lim50_2100/SOCinc_2020_perha_permgrass_2100")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim25_2050",
    query_column="SOCinc_2020_perha_2y_lim25_2050/SOCinc_2020_perha_permgrass_2050")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim25_2080",
    query_column="SOCinc_2020_perha_2y_lim25_2080/SOCinc_2020_perha_permgrass_2080")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_2y_lim25_2100",
    query_column="SOCinc_2020_perha_2y_lim25_2100/SOCinc_2020_perha_permgrass_2100")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_3y_2050",
    query_column="SOCinc_2020_perha_3y_2050/SOCinc_2020_perha_permgrass_2050")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_3y_2080",
    query_column="SOCinc_2020_perha_3y_2080/SOCinc_2020_perha_permgrass_2080")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_3y_2100",
    query_column="SOCinc_2020_perha_3y_2100/SOCinc_2020_perha_permgrass_2100")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_4y_2050",
    query_column="SOCinc_2020_perha_4y_2050/SOCinc_2020_perha_permgrass_2050")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_4y_2080",
    query_column="SOCinc_2020_perha_4y_2080/SOCinc_2020_perha_permgrass_2080")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_4y_2100",
    query_column="SOCinc_2020_perha_4y_2100/SOCinc_2020_perha_permgrass_2100")

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="comp_max_SOCinc_low_est_2050 double precision,comp_max_SOCinc_low_est_2080 double precision,comp_max_SOCinc_low_est_2100 double precision,\
            comp_max_SOCinc_high_est_2050 double precision,comp_max_SOCinc_high_est_2080 double precision,comp_max_SOCinc_high_est_2100 double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_low_est_2050",
    query_column="SOCinc_2020_perha_low_est_2050/SOCinc_2020_perha_permgrass_2050")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_low_est_2080",
    query_column="SOCinc_2020_perha_low_est_2080/SOCinc_2020_perha_permgrass_2080")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_low_est_2100",
    query_column="SOCinc_2020_perha_low_est_2100/SOCinc_2020_perha_permgrass_2100")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_high_est_2050",
    query_column="SOCinc_2020_perha_high_est_2050/SOCinc_2020_perha_permgrass_2050")

    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_high_est_2080",
    query_column="SOCinc_2020_perha_high_est_2080/SOCinc_2020_perha_permgrass_2080")
    
    Module("v.db.update",
    map=vectoutmap,
    column="comp_max_SOCinc_high_est_2100",
    query_column="SOCinc_2020_perha_high_est_2100/SOCinc_2020_perha_permgrass_2100")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n comp_max_SOCinc() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)

#######################################
#
#
# Functions for calculating co-benefits
#
#
#######################################

def water_erosion():
    start_time = time.time()

    """
    Assumption: water erosion is marginal in ley production
    Thus, water erosion is reduced with the share of annual crops under ley
    Share of annual crops under ley calculated in area():
        2y: 1/3
        2y_lim50: 1/6
        2y_lim25: 1/12
        3y: 3/7
        4y: 1/2
    """
    
#### per hectare
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_red_perha_2y double precision,water_erosion_red_perha_2y_lim50 double precision,\
        water_erosion_red_perha_2y_lim25 double precision,water_erosion_red_perha_3y double precision,water_erosion_red_perha_4y double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_2y",
    query_column="water_erosion_source/3")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_2y_lim50",
    query_column="water_erosion_red_perha_2y/2")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_2y_lim25",
    query_column="water_erosion_red_perha_2y/4")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_3y",
    query_column="water_erosion_source*3/7")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_4y",
    query_column="water_erosion_source/2")

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_red_perha_low_est double precision,water_erosion_red_perha_high_est double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_low_est",
    query_column="water_erosion_source*low_est_area_factor")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_perha_high_est",
    query_column="water_erosion_source*high_est_area_factor")

#### in total
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_red_total_2y int,water_erosion_red_total_2y_lim50 int,\
        water_erosion_red_total_2y_lim25 int,water_erosion_red_total_3y int,water_erosion_red_total_4y int"
    )

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_2y",
    query_column="water_erosion_red_perha_2y*annual_crops_number")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_2y_lim50",
    query_column="water_erosion_red_perha_2y_lim50*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_2y_lim25",
    query_column="water_erosion_red_perha_2y_lim25*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_3y",
    query_column="water_erosion_red_perha_3y*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_4y",
    query_column="water_erosion_red_perha_4y*annual_crops_number")
    
# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_red_total_low_est double precision,water_erosion_red_total_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_low_est",
    query_column="water_erosion_red_perha_low_est*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_red_total_high_est",
    query_column="water_erosion_red_perha_high_est*annual_crops_number")
    
#### contribution to reaching a low impact

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_towardsLow_perha_2y double precision,water_erosion_towardsLow_perha_2y_lim50 double precision,\
        water_erosion_towardsLow_perha_2y_lim25 double precision,water_erosion_towardsLow_perha_3y double precision,water_erosion_towardsLow_perha_4y double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_2y",
    query_column="water_erosion_red_perha_2y/aboveLow_water_erosion")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_2y_lim50",
    query_column="water_erosion_red_perha_2y_lim50/aboveLow_water_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_2y_lim25",
    query_column="water_erosion_red_perha_2y_lim25/aboveLow_water_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_3y",
    query_column="water_erosion_red_perha_3y/aboveLow_water_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_4y",
    query_column="water_erosion_red_perha_4y/aboveLow_water_erosion")

    
# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="water_erosion_towardsLow_perha_low_est double precision,water_erosion_towardsLow_perha_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_low_est",
    query_column="water_erosion_red_perha_low_est/aboveLow_water_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="water_erosion_towardsLow_perha_high_est",
    query_column="water_erosion_red_perha_high_est/aboveLow_water_erosion")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n ...water_erosion() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def wind_erosion():
    start_time = time.time()

    """
    See water erosion
    """
    
#### per hectare
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_red_perha_2y double precision,wind_erosion_red_perha_2y_lim50 double precision,\
        wind_erosion_red_perha_2y_lim25 double precision,wind_erosion_red_perha_3y double precision,wind_erosion_red_perha_4y double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_2y",
    query_column="wind_erosion_source/3")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_2y_lim50",
    query_column="wind_erosion_red_perha_2y/2")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_2y_lim25",
    query_column="wind_erosion_red_perha_2y/4")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_3y",
    query_column="wind_erosion_source*3/7")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_4y",
    query_column="wind_erosion_source/2")
    
# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_red_perha_low_est double precision,wind_erosion_red_perha_high_est double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_low_est",
    query_column="wind_erosion_source*low_est_area_factor")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_perha_high_est",
    query_column="wind_erosion_source*high_est_area_factor")
#### in total
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_red_total_2y int,wind_erosion_red_total_2y_lim50 int,\
        wind_erosion_red_total_2y_lim25 int,wind_erosion_red_total_3y int,wind_erosion_red_total_4y int")
        
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_2y",
    query_column="wind_erosion_red_perha_2y*annual_crops_number")
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_2y_lim50",
    query_column="wind_erosion_red_perha_2y_lim50*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_2y_lim25",
    query_column="wind_erosion_red_perha_2y_lim25*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_3y",
    query_column="wind_erosion_red_perha_3y*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_4y",
    query_column="wind_erosion_red_perha_4y*annual_crops_number")

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_red_total_low_est double precision,wind_erosion_red_total_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_low_est",
    query_column="wind_erosion_red_perha_low_est*annual_crops_number")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_red_total_high_est",
    query_column="wind_erosion_red_perha_high_est*annual_crops_number")
    
#### contribution to reaching a low impact

    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_towardsLow_perha_2y double precision,wind_erosion_towardsLow_perha_2y_lim50 double precision,\
        wind_erosion_towardsLow_perha_2y_lim25 double precision,wind_erosion_towardsLow_perha_3y double precision,wind_erosion_towardsLow_perha_4y double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_2y",
    query_column="wind_erosion_red_perha_2y/aboveLow_wind_erosion")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_2y_lim50",
    query_column="wind_erosion_red_perha_2y_lim50/aboveLow_wind_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_2y_lim25",
    query_column="wind_erosion_red_perha_2y_lim25/aboveLow_wind_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_3y",
    query_column="wind_erosion_red_perha_3y/aboveLow_wind_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_4y",
    query_column="wind_erosion_red_perha_4y/aboveLow_wind_erosion")

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="wind_erosion_towardsLow_perha_low_est double precision,wind_erosion_towardsLow_perha_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_low_est",
    query_column="wind_erosion_red_perha_low_est/aboveLow_wind_erosion")
    
    Module("v.db.update",
    map=vectoutmap,
    column="wind_erosion_towardsLow_perha_high_est",
    query_column="wind_erosion_red_perha_high_est/aboveLow_wind_erosion")

    elapsed_time = time.time() - start_time    
    print(Fore.CYAN + "\n ...wind_erosion() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def N_emissions():
    start_time = time.time()

    """
    See water erosion.
    When calculating total values, perha is multiplied with total area instead of annual crop area. See methods.
    """

    N_leaching_coeff = "0.75"

    #### per hectare
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="N_emissions_red_perha_2y double precision,N_emissions_red_perha_2y_lim50 double precision,\
        N_emissions_red_perha_2y_lim25 double precision,N_emissions_red_perha_3y double precision,N_emissions_red_perha_4y double precision")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_2y",
    query_column="N_emissions_source/3*"+N_leaching_coeff)

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_2y_lim50",
    query_column="N_emissions_red_perha_2y/2*"+N_leaching_coeff)

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_2y_lim25",
    query_column="N_emissions_red_perha_2y/4*"+N_leaching_coeff)

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_3y",
    query_column="N_emissions_source*3/7*"+N_leaching_coeff)

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_4y",
    query_column="N_emissions_source/2*"+N_leaching_coeff)

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="N_emissions_red_perha_low_est double precision,N_emissions_red_perha_high_est double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_low_est",
    query_column="N_emissions_source*low_est_area_factor*"+N_leaching_coeff)
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_perha_high_est",
    query_column="N_emissions_source*high_est_area_factor*"+N_leaching_coeff)
    
#### in total
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="N_emissions_red_total_2y int,N_emissions_red_total_2y_lim50 int,\
        N_emissions_red_total_2y_lim25 int,N_emissions_red_total_3y int,N_emissions_red_total_4y int")
        
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_2y",
    query_column="N_emissions_red_perha_2y*area")

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_2y_lim50",
    query_column="N_emissions_red_perha_2y_lim50*area")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_2y_lim25",
    query_column="N_emissions_red_perha_2y_lim25*area")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_3y",
    query_column="N_emissions_red_perha_3y*area")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_4y",
    query_column="N_emissions_red_perha_4y*area")

# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="N_emissions_red_total_low_est double precision,N_emissions_red_total_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_low_est",
    query_column="N_emissions_red_perha_low_est*area")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_red_total_high_est",
    query_column="N_emissions_red_perha_high_est*area")

#### contribution to reaching a low impact

    Module("v.db.addcolumn",
    map=vectoutmap, 
    columns="N_emissions_towardsLow_perha_2y double precision,N_emissions_towardsLow_perha_2y_lim50 double precision,\
        N_emissions_towardsLow_perha_2y_lim25 double precision,N_emissions_towardsLow_perha_3y double precision,N_emissions_towardsLow_perha_4y double precision")
        
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_2y",
    query_column="N_emissions_red_perha_2y/aboveLow_N_emissions")

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_2y_lim50",
    query_column="N_emissions_red_perha_2y_lim50/aboveLow_N_emissions")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_2y_lim25",
    query_column="N_emissions_red_perha_2y_lim25/aboveLow_N_emissions")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_3y",
    query_column="N_emissions_red_perha_3y/aboveLow_N_emissions")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_4y",
    query_column="N_emissions_red_perha_4y/aboveLow_N_emissions")
    
# Scenarios    
    
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="N_emissions_towardsLow_perha_low_est double precision,N_emissions_towardsLow_perha_high_est double precision")

    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_low_est",
    query_column="N_emissions_red_perha_low_est/aboveLow_N_emissions")
    
    Module("v.db.update",
    map=vectoutmap,
    column="N_emissions_towardsLow_perha_high_est",
    query_column="N_emissions_red_perha_high_est/aboveLow_N_emissions")
    
    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n ...N_emissions() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)
    
def flooding():
    start_time = time.time()
    
    # See methods
       
    Module("v.db.addcolumn", 
    map=vectoutmap, 
    columns="flooding_red int")
    
    Module("v.db.update",
    map=vectoutmap,
    column="flooding_red",
    query_column="effectiveness_flooding")

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n ...flooding() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)

    
def export_selected():
    start_time = time.time()
    
    # save suitable landscapes in GRASS
    
    gscript.run_command("v.extract", input=vectoutmap, output=vectoutmap_suitable,\
                        where="effectiveness_SOC_sat_cap >1 AND EU28 =1", overwrite=True)

    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n ...export_selected() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)

def export_gpkg():

    # export selected to gpkg    
    start_time = time.time()

    gscript.run_command("v.out.ogr", input=vectoutmap_suitable, output=export_path_gpkg,\
                        format="GPKG", output_layer=vectoutmap_suitable, flags='u', overwrite=True)
    
    elapsed_time = time.time() - start_time    
    print(Fore.CYAN + "\n ...export_gpkg() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)                        
        
def export_csv():
    start_time = time.time()
    
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"basic.csv",\
                        columns="country,sum(annual_crops_number) as sum_annual, sum(area_2y), sum(area_2y_lim50),sum(area_2y_lim25),sum(area_3y),sum(area_4y),sum(low_est_area),sum(high_est_area),\
                            sum(biomass_2y), sum(biomass_2y_lim50), sum(biomass_2y_lim25), sum(biomass_3y), sum(biomass_4y), sum(low_est_biomass), sum(high_est_biomass)",\
                        group="country",
                        overwrite=True)
              
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"SOCinc_BAU.csv",\
                        columns="country,avg(SOCinc_BAU_perha_2y_2050), avg(SOCinc_BAU_perha_3y_2050),avg(SOCinc_BAU_perha_4y_2050),avg(SOCinc_BAU_perha_permgrass_2050),avg(SOCinc_BAU_perha_low_est_2050),avg(SOCinc_BAU_perha_high_est_2050),\
                                avg(SOCinc_BAU_perha_2y_2080), avg(SOCinc_BAU_perha_3y_2080),avg(SOCinc_BAU_perha_4y_2080),avg(SOCinc_BAU_perha_permgrass_2080),avg(SOCinc_BAU_perha_low_est_2080),avg(SOCinc_BAU_perha_high_est_2080),\
                                avg(SOCinc_BAU_perha_2y_2100), avg(SOCinc_BAU_perha_3y_2100),avg(SOCinc_BAU_perha_4y_2100),avg(SOCinc_BAU_perha_permgrass_2100),avg(SOCinc_BAU_perha_low_est_2100),avg(SOCinc_BAU_perha_high_est_2100),\
                                sum(SOCinc_BAU_total_2y_2050), sum(SOCinc_BAU_total_3y_2050),sum(SOCinc_BAU_total_4y_2050),sum(SOCinc_BAU_total_permgrass_2050),sum(SOCinc_BAU_total_low_est_2050),sum(SOCinc_BAU_total_high_est_2050),\
                                sum(SOCinc_BAU_total_2y_2080), sum(SOCinc_BAU_total_3y_2080),sum(SOCinc_BAU_total_4y_2080),sum(SOCinc_BAU_total_permgrass_2080),sum(SOCinc_BAU_total_low_est_2080),sum(SOCinc_BAU_total_high_est_2080),\
                                sum(SOCinc_BAU_total_2y_2100), sum(SOCinc_BAU_total_3y_2100),sum(SOCinc_BAU_total_4y_2100),sum(SOCinc_BAU_total_permgrass_2100),sum(SOCinc_BAU_total_low_est_2100),sum(SOCinc_BAU_total_high_est_2100)",\
                        group="country",
                        overwrite=True)
        
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"SOCinc_2020.csv",\
                        columns="country,avg(SOCinc_2020_perha_2y_2050), avg(SOCinc_2020_perha_3y_2050),avg(SOCinc_2020_perha_4y_2050),avg(SOCinc_2020_perha_permgrass_2050),avg(SOCinc_2020_perha_low_est_2050),avg(SOCinc_2020_perha_high_est_2050),\
                                avg(SOCinc_2020_perha_2y_2080), avg(SOCinc_2020_perha_3y_2080),avg(SOCinc_2020_perha_4y_2080),avg(SOCinc_2020_perha_permgrass_2080),avg(SOCinc_2020_perha_low_est_2080),avg(SOCinc_2020_perha_high_est_2080),\
                                avg(SOCinc_2020_perha_2y_2100), avg(SOCinc_2020_perha_3y_2100),avg(SOCinc_2020_perha_4y_2100),avg(SOCinc_2020_perha_permgrass_2100),avg(SOCinc_2020_perha_low_est_2100),avg(SOCinc_2020_perha_high_est_2100),\
                                sum(SOCinc_2020_total_2y_2050), sum(SOCinc_2020_total_3y_2050),sum(SOCinc_2020_total_4y_2050),sum(SOCinc_2020_total_permgrass_2050),sum(SOCinc_2020_total_low_est_2050),sum(SOCinc_2020_total_high_est_2050),\
                                sum(SOCinc_2020_total_2y_2080), sum(SOCinc_2020_total_3y_2080),sum(SOCinc_2020_total_4y_2080),sum(SOCinc_2020_total_permgrass_2080),sum(SOCinc_2020_total_low_est_2080),sum(SOCinc_2020_total_high_est_2080),\
                                sum(SOCinc_2020_total_2y_2100), sum(SOCinc_2020_total_3y_2100),sum(SOCinc_2020_total_4y_2100),sum(SOCinc_2020_total_permgrass_2100),sum(SOCinc_2020_total_low_est_2100),sum(SOCinc_2020_total_high_est_2100)",\
                        group="country",
                        overwrite=True)
    
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"cobenefits.csv",\
                        columns="country,avg(water_erosion_red_perha_2y),avg(water_erosion_red_perha_3y),avg(water_erosion_red_perha_4y),avg(water_erosion_red_perha_low_est),avg(water_erosion_red_perha_high_est),\
                                sum(water_erosion_red_total_2y),sum(water_erosion_red_total_3y),sum(water_erosion_red_total_4y),sum(water_erosion_red_total_low_est),sum(water_erosion_red_total_high_est),\
                                avg(wind_erosion_red_perha_2y),avg(wind_erosion_red_perha_3y),avg(wind_erosion_red_perha_4y),avg(wind_erosion_red_perha_low_est),avg(wind_erosion_red_perha_high_est),\
                                sum(wind_erosion_red_total_2y),sum(wind_erosion_red_total_3y),sum(wind_erosion_red_total_4y),sum(wind_erosion_red_total_low_est),sum(wind_erosion_red_total_high_est),\
                                avg(N_emissions_red_perha_2y),avg(N_emissions_red_perha_3y),avg(N_emissions_red_perha_4y),avg(N_emissions_red_perha_low_est),avg(N_emissions_red_perha_high_est),\
                                sum(N_emissions_red_total_2y),sum(N_emissions_red_total_3y),sum(N_emissions_red_total_4y),sum(N_emissions_red_total_low_est),sum(N_emissions_red_total_high_est)",\
                        group="country",
                        overwrite=True)
    
    # EU total values, for comparison
        
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"basic_EU.csv",\
                        columns="sum(annual_crops_number) as sum_annual, sum(area_2y), sum(area_2y_lim50),sum(area_2y_lim25),sum(area_3y),sum(area_4y),sum(low_est_area),sum(high_est_area),\
                            sum(biomass_2y), sum(biomass_2y_lim50), sum(biomass_2y_lim25), sum(biomass_3y), sum(biomass_4y), sum(low_est_biomass), sum(high_est_biomass)",\
                        overwrite=True)
        
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"SOCinc_BAU_EU.csv",\
                        columns="avg(SOCinc_BAU_perha_2y_2050), avg(SOCinc_BAU_perha_3y_2050),avg(SOCinc_BAU_perha_4y_2050),avg(SOCinc_BAU_perha_permgrass_2050),avg(SOCinc_BAU_perha_low_est_2050),avg(SOCinc_BAU_perha_high_est_2050),\
                                avg(SOCinc_BAU_perha_2y_2080), avg(SOCinc_BAU_perha_3y_2080),avg(SOCinc_BAU_perha_4y_2080),avg(SOCinc_BAU_perha_permgrass_2080),avg(SOCinc_BAU_perha_low_est_2080),avg(SOCinc_BAU_perha_high_est_2080),\
                                avg(SOCinc_BAU_perha_2y_2100), avg(SOCinc_BAU_perha_3y_2100),avg(SOCinc_BAU_perha_4y_2100),avg(SOCinc_BAU_perha_permgrass_2100),avg(SOCinc_BAU_perha_low_est_2100),avg(SOCinc_BAU_perha_high_est_2100),\
                                sum(SOCinc_BAU_total_2y_2050), sum(SOCinc_BAU_total_3y_2050),sum(SOCinc_BAU_total_4y_2050),sum(SOCinc_BAU_total_permgrass_2050),sum(SOCinc_BAU_total_low_est_2050),sum(SOCinc_BAU_total_high_est_2050),\
                                sum(SOCinc_BAU_total_2y_2080), sum(SOCinc_BAU_total_3y_2080),sum(SOCinc_BAU_total_4y_2080),sum(SOCinc_BAU_total_permgrass_2080),sum(SOCinc_BAU_total_low_est_2080),sum(SOCinc_BAU_total_high_est_2080),\
                                sum(SOCinc_BAU_total_2y_2100), sum(SOCinc_BAU_total_3y_2100),sum(SOCinc_BAU_total_4y_2100),sum(SOCinc_BAU_total_permgrass_2100),sum(SOCinc_BAU_total_low_est_2100),sum(SOCinc_BAU_total_high_est_2100)",\
                        overwrite=True)
        
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"SOCinc_2020_EU.csv",\
                        columns="avg(SOCinc_2020_perha_2y_2050), avg(SOCinc_2020_perha_3y_2050),avg(SOCinc_2020_perha_4y_2050),avg(SOCinc_2020_perha_permgrass_2050),avg(SOCinc_2020_perha_low_est_2050),avg(SOCinc_2020_perha_high_est_2050),\
                                avg(SOCinc_2020_perha_2y_2080), avg(SOCinc_2020_perha_3y_2080),avg(SOCinc_2020_perha_4y_2080),avg(SOCinc_2020_perha_permgrass_2080),avg(SOCinc_2020_perha_low_est_2080),avg(SOCinc_2020_perha_high_est_2080),\
                                avg(SOCinc_2020_perha_2y_2100), avg(SOCinc_2020_perha_3y_2100),avg(SOCinc_2020_perha_4y_2100),avg(SOCinc_2020_perha_permgrass_2100),avg(SOCinc_2020_perha_low_est_2100),avg(SOCinc_2020_perha_high_est_2100),\
                                sum(SOCinc_2020_total_2y_2050), sum(SOCinc_2020_total_3y_2050),sum(SOCinc_2020_total_4y_2050),sum(SOCinc_2020_total_permgrass_2050),sum(SOCinc_2020_total_low_est_2050),sum(SOCinc_2020_total_high_est_2050),\
                                sum(SOCinc_2020_total_2y_2080), sum(SOCinc_2020_total_3y_2080),sum(SOCinc_2020_total_4y_2080),sum(SOCinc_2020_total_permgrass_2080),sum(SOCinc_2020_total_low_est_2080),sum(SOCinc_2020_total_high_est_2080),\
                                sum(SOCinc_2020_total_2y_2100), sum(SOCinc_2020_total_3y_2100),sum(SOCinc_2020_total_4y_2100),sum(SOCinc_2020_total_permgrass_2100),sum(SOCinc_2020_total_low_est_2100),sum(SOCinc_2020_total_high_est_2100)",\
                        overwrite=True)
    
    gscript.run_command("v.db.select", map=vectoutmap_suitable, file=export_path_calculations+"cobenefits_EU.csv",\
                        columns="avg(water_erosion_red_perha_2y),avg(water_erosion_red_perha_3y),avg(water_erosion_red_perha_4y),avg(water_erosion_red_perha_low_est),avg(water_erosion_red_perha_high_est),\
                                sum(water_erosion_red_total_2y),sum(water_erosion_red_total_3y),sum(water_erosion_red_total_4y),sum(water_erosion_red_total_low_est),sum(water_erosion_red_total_high_est),\
                                avg(wind_erosion_red_perha_2y),avg(wind_erosion_red_perha_3y),avg(wind_erosion_red_perha_4y),avg(wind_erosion_red_perha_low_est),avg(wind_erosion_red_perha_high_est),\
                                sum(wind_erosion_red_total_2y),sum(wind_erosion_red_total_3y),sum(wind_erosion_red_total_4y),sum(wind_erosion_red_total_low_est),sum(wind_erosion_red_total_high_est),\
                                avg(N_emissions_red_perha_2y),avg(N_emissions_red_perha_3y),avg(N_emissions_red_perha_4y),avg(N_emissions_red_perha_low_est),avg(N_emissions_red_perha_high_est),\
                                sum(N_emissions_red_total_2y),sum(N_emissions_red_total_3y),sum(N_emissions_red_total_4y),sum(N_emissions_red_total_low_est),sum(N_emissions_red_total_high_est)",\
                        overwrite=True)
    
    elapsed_time = time.time() - start_time
    print(Fore.CYAN + "\n ...export_csv() completed... \n Elapsed time:", elapsed_time,"seconds\n")
    print(Fore.WHITE)   

##################################################################
# 
#                            GUI
#
##################################################################
"""
def counter():
    elapsed_time = int(time.time() - start_time)
    return str(elapsed_time)
"""
a= Tk()  
a.geometry("800x800") 

CheckVar1 = IntVar()  
CheckVar2 = IntVar()  
CheckVar3 = IntVar()  
CheckVar4 = IntVar()  
CheckVar5 = IntVar()  
CheckVar6 = IntVar()
CheckVar7 = IntVar()  
CheckVar8 = IntVar()  
CheckVar9 = IntVar()
CheckVar10 = IntVar()
CheckVar11 = IntVar()
CheckVar12 = IntVar()

notcompleted ="Not completed"
running = "Running..."
completed = "--------> Completed: "

L0 = Label(a, text="\nSelect operation\n")
L1 = Label(a, text=notcompleted)
L2 = Label(a, text=notcompleted) 
L3 = Label(a, text=notcompleted)   
L4 = Label(a, text=notcompleted)  
L5 = Label(a, text=notcompleted)   
L6 = Label(a, text=notcompleted)  
L7 = Label(a, text=notcompleted)    
L8 = Label(a, text=notcompleted)
L9 = Label(a, text=notcompleted)
L10 = Label(a, text=notcompleted)
L11 = Label(a, text=notcompleted)
L12 = Label(a, text=notcompleted)

###############
#
# GUI functions
#
###############


def selected_1():
    start_time = time.time()

    L1.config(text=running) 
    L1.update_idletasks()
    
    start_over()
    
    L1.config(text=completed+get_time()) 
    L1.update_idletasks()
    
    labels = [L2,L3,L4,L5,L6,L7,L8,L9,L10,L11,L12]
    
    for label in labels:
        label.config(text="Not completed")
        label.update_idletasks()
      
def selected_2():
    L2.config(text=running) 
    L2.update_idletasks()
    
    area()
    
    L2.config(text=completed+get_time()) 
    L2.update_idletasks()

def selected_3():
    L3.config(text=running) 
    L3.update_idletasks()
    
    biomass()
    
    L3.config(text=completed+get_time()) 
    L3.update_idletasks()
    
def selected_4():
    L4.config(text=running) 
    L4.update_idletasks()
    
    SOC_increase_relative_BAU()
    
    L4.config(text=completed+get_time())   
    L3.update_idletasks()

def selected_5():
    L5.config(text=running) 
    L5.update_idletasks()
    
    SOC_increase_relative_2020()
    
    L5.config(text=completed+get_time()) 
    L3.update_idletasks()    

def selected_6():
    L6.config(text=running) 
    L6.update_idletasks()
    
    SOC_values_perha()
    
    L6.config(text=completed+get_time()) 
    L3.update_idletasks()    

def selected_7():
    L7.config(text=running) 
    L7.update_idletasks()
    
    comp_max_SOCinc()
    
    L7.config(text=completed+get_time()) 
    L3.update_idletasks()    

def selected_8():
    L8.config(text=running+" (1/4: water erosion)")
    L8.update_idletasks()
    
    water_erosion()
    
    L8.config(text=running+" (2/4: wind erosion)")
    L8.update_idletasks()
    
    # wind_erosion()
    
    L8.config(text=running+" (3/4: N emissions)")
    L8.update_idletasks()
    
    # N_emissions()
    
    L8.config(text=running+" (4/4: Flooding)")
    L8.update_idletasks()
    
    # flooding()
    
    L8.config(text=completed+get_time()) 
    L8.update_idletasks()
    
def selected_9():
    labels = [L2,L3,L4,L5,L6,L7,L8]
    for label in labels:
        label.config(text="Waiting")
        label.update_idletasks()
        
    L9.config(text=running+" (1/7)")
    L9.update_idletasks()
    selected_2()
    
    L9.config(text=running+" (2/7)") 
    L9.update_idletasks()
    selected_3()
 
    L9.config(text=running+" (3/7)") 
    L9.update_idletasks()
    selected_4()
    
    L9.config(text=running+" (4/7)") 
    L9.update_idletasks()
    selected_5()
    
    L9.config(text=running+" (5/7)") 
    L9.update_idletasks()
    selected_6()
    
    L9.config(text=running+" (6/7)") 
    L9.update_idletasks()
    selected_7()
        
    L9.config(text=running+" (7/7)") 
    L9.update_idletasks() 
    selected_8()
    
    L9.config(text=completed+get_time()) 
    L9.update_idletasks()

def selected_10():
    L10.config(text=running + " (1/2: selected to grass)") 
    L10.update_idletasks()
   
    export_selected()
    
    L10.config(text=running + " (2/2: selected to gpkg)") 
    L10.update_idletasks()

    export_gpkg()

    L10.config(text=completed+get_time()) 
    L10.update_idletasks() 

def selected_11():
    L11.config(text=running) 
    L11.update_idletasks()
    
    export_csv()
    
    L11.config(text=completed+get_time()) 
    L11.update_idletasks()

def selected_12():
    labels = [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10,L11]

    for label in labels:
        label.config(text="Not completed")
        label.update_idletasks()
        
def selected_13():
    L12.config(text=running) 
    L12.update_idletasks()
    
    scenarios()
    
    L12.config(text=completed+get_time()) 
    L12.update_idletasks()
    
 
C1 = Checkbutton(a, text = "Start over",activebackground="black", activeforeground="WHITE",\
                 bg="CYAN",width=35,bd=10,variable = CheckVar1,onvalue=1,offvalue=0,\
                     command = selected_1)

C2 = Checkbutton(a, text = "Calculate areas",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar2,onvalue = 1, offvalue = 0,\
                     command = selected_2) 

C3 = Checkbutton(a, text = "Calculate biomass",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar3,onvalue = 1, offvalue = 0,\
                     command = selected_3)
    
C4 = Checkbutton(a, text = "Calculate SOC increase relative BAU",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar4,onvalue = 1, offvalue = 0,\
                     command = selected_4)

C5 = Checkbutton(a, text = "Calculate SOC increase relative 2020",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar5,onvalue = 1, offvalue = 0,\
                     command = selected_5)

C6 = Checkbutton(a, text = "Calculate new SOC values per ha",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar6,onvalue = 1, offvalue = 0,\
                     command = selected_6) 

C7 = Checkbutton(a, text = "Calculate % of max SOC increase",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar7,onvalue = 1, offvalue = 0,\
                     command = selected_7)
    
C8 = Checkbutton(a, text = "Calculate co-benefits",activebackground="black", activeforeground="WHITE",\
                 bg="lightgreen",width=35,bd=10,variable = CheckVar8,onvalue = 1, offvalue = 0,\
                     command = selected_8)

C9 = Checkbutton(a, text = "Calculate all",activebackground="black", activeforeground="WHITE",foreground="WHITE",\
                 bg="green",width=35,bd=10,variable = CheckVar9,onvalue = 1, offvalue = 0,\
                     command = selected_9) 

C10 = Checkbutton(a, text = "Export to gpkg",activebackground="black", activeforeground="WHITE",\
                 bg="yellow",width=35,bd=10,variable = CheckVar10,onvalue = 1, offvalue = 0,\
                     command = selected_10)

C11 = Checkbutton(a, text = "Aggregate and export to csv",activebackground="black", activeforeground="WHITE",\
                 bg="yellow",width=35,bd=10,variable = CheckVar11,onvalue = 1, offvalue = 0,\
                     command = selected_11)

C12 = Checkbutton(a, text = "Reset fields",activebackground="black", activeforeground="WHITE",\
                 bg="RED",width=35,bd=10,variable = CheckVar12,onvalue = 1, offvalue = 0,\
                     command = selected_12)
    
C13 = Checkbutton(a, text = "Quit",activebackground="black", activeforeground="WHITE",\
                 bg="RED",width=35,bd=10,variable = CheckVar12,onvalue = 1, offvalue = 0,\
                     command = a.destroy)

C14 = Checkbutton(a, text = "Prepare scenarios",activebackground="black", activeforeground="WHITE",\
                 bg="lightblue",width=35,bd=10,variable = CheckVar12,onvalue = 1, offvalue = 0,\
                     command = selected_13)
    
C1.grid(row=1,column=0)
C14.grid(row=2,column=0)
C2.grid(row=3,column=0)
C3.grid(row=4,column=0)
C4.grid(row=5,column=0)
C5.grid(row=6,column=0)
C6.grid(row=7,column=0)
C7.grid(row=8,column=0)
C8.grid(row=9,column=0)
C9.grid(row=10,column=0)
C10.grid(row=11,column=0)
C11.grid(row=12,column=0)
C12.grid(row=13,column=0)
C13.grid(row=14,column=0)


L0.grid(row=0,column=0)   
L1.grid(row=1,column=1)   
L12.grid(row=2,column=1)   
L2.grid(row=3,column=1)    
L3.grid(row=4,column=1)    
L4.grid(row=5,column=1)    
L5.grid(row=6,column=1)    
L6.grid(row=7,column=1)    
L7.grid(row=8,column=1)        
L8.grid(row=9,column=1)  
L9.grid(row=10,column=1)  
L10.grid(row=11,column=1)
L11.grid(row=12,column=1)  

a.mainloop()

