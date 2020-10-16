--                                                                            
-- VHDL netlist for design DPT                           
-- Created by the Saber Integration Toolkit         0 of Synopsys, Inc.     
-- Created on Thu Oct 15 16:52:12 2020.                                       
--                                                                            

PACKAGE design_pkg is
  constant lg_hi : real;
  constant lg_low : real;
  constant rshunt : real;
  constant lb : real;
  constant ccoeff : real;
END PACKAGE design_pkg;

PACKAGE body design_pkg is
  constant lg_hi : real := 1.409000e-09;
  constant lg_low : real := 6.710000e+00;
  constant rshunt : real := 5.000000e-01;
  constant lb : real := 3.715000e-09;
  constant ccoeff : real := 1.0;
END PACKAGE BODY design_pkg;




------------------------------------
-- Description for 'DPT' 
------------------------------------


--
--  Structural description for 'DPT'.
--
LIBRARY ieee;
USE ieee.electrical_systems.all;
library ai_electronic;
library ai_std;
use ai_std.ai_standard.all;
use ai_std.semiconductor_devices.all;
LIBRARY vhdl_utility;
USE vhdl_utility.statistics.all;

ENTITY DPT IS
END DPT;

ARCHITECTURE struct OF DPT IS

  -- Internal buses of this cell.

  -- Internal signals of this cell.
  TERMINAL n_739 : electrical ;
  TERMINAL n_555 : electrical ;
  TERMINAL n_153 : electrical ;
  TERMINAL d : electrical ;
  TERMINAL n_743 : electrical ;
  TERMINAL n_744 : electrical ;
  TERMINAL n_730 : electrical ;
  TERMINAL s : electrical ;
  TERMINAL n_189 : electrical ;
  TERMINAL n_550 : electrical ;
  TERMINAL n_333 : electrical ;
  TERMINAL n_1 : electrical ;
  TERMINAL freeNet1 : electrical ;
  TERMINAL freeNet2 : electrical ;

  -- Constants for this cell.
  constant lg_hi : real := work.design_pkg.lg_hi;
  constant lg_low : real := work.design_pkg.lg_low;
  constant rshunt : real := work.design_pkg.rshunt;
  constant lb : real := work.design_pkg.lb;
  constant ccoeff : real := work.design_pkg.ccoeff;


BEGIN
   resistor2 : ENTITY ai_electronic.resistor(behavioral) 
      GENERIC MAP (
        rnom => 1.625000e-01,
        model => r_default_model_init,
        l => 0.0,
        w => 0.0,
        scalm => 1.0,
        dtemp => 0.0,
        scale => 1.0,
        tc2 => 0.0,
        temp => AMBIENT_TEMPERATURE,
        tc1 => 0.0,
        multp => 1.0)
      PORT MAP (
        p => freeNet1,
        m => freeNet2);

   MAST : ENTITY work.DPT_MAST
      GENERIC MAP (
        lg_hi => lg_hi,
        lg_low => lg_low,
        rshunt => rshunt,
        lb => lb,
        ccoeff => ccoeff)
      PORT MAP (
        n_739,
        n_1,
        n_333,
        n_550,
        n_189,
        s,
        n_730,
        n_744,
        n_743,
        d,
        n_153,
        n_555);
END struct;
