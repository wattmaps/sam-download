from PySSC import PySSC
if __name__ == "__main__":
	ssc = PySSC()
	print ('Current folder = \\esm.ucsb.edu/meds/meds2023/michellelam/Python Scripts')
	print ('SSC Version = ', ssc.version())
	print ('SSC Build Information = ', ssc.build_info().decode("utf - 8"))
	ssc.module_exec_set_print(0)
	data = ssc.data_create()
	ssc.data_set_string( data, b'solar_resource_file', b'C:/SAM/2022.11.21/solar_resource/phoenix_az_33.450495_-111.983688_psmv3_60_tmy.csv' );
	albedo =[ 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001, 0.20000000000000001 ];
	ssc.data_set_array( data, b'albedo',  albedo);
	ssc.data_set_number( data, b'use_wf_albedo', 1 )
	ssc.data_set_number( data, b'system_capacity', 50000 )
	ssc.data_set_number( data, b'module_type', 0 )
	ssc.data_set_number( data, b'dc_ac_ratio', 1.3400000000000001 )
	ssc.data_set_number( data, b'bifaciality', 0 )
	ssc.data_set_number( data, b'array_type', 2 )
	ssc.data_set_number( data, b'tilt', 0 )
	ssc.data_set_number( data, b'azimuth', 180 )
	ssc.data_set_number( data, b'gcr', 0.29999999999999999 )
	soiling =[ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ];
	ssc.data_set_array( data, b'soiling',  soiling);
	ssc.data_set_number( data, b'losses', 12.304024826166826 )
	ssc.data_set_number( data, b'en_snowloss', 0 )
	ssc.data_set_number( data, b'inv_eff', 98 )
	ssc.data_set_number( data, b'batt_simple_enable', 0 )
	ssc.data_set_number( data, b'adjust:constant', 0 )
	ssc.data_set_array_from_csv( data, b'grid_curtailment', b'\\esm.ucsb.edu/meds/meds2023/michellelam/Python Scripts/grid_curtailment.csv');
	ssc.data_set_number( data, b'enable_interconnection_limit', 0 )
	ssc.data_set_number( data, b'grid_interconnection_limit_kwac', 100000 )
	module = ssc.module_create(b'pvwattsv8')	
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('pvwattsv8 simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	module = ssc.module_create(b'grid')	
	ssc.module_exec_set_print( 0 );
	if ssc.module_exec(module, data) == 0:
		print ('grid simulation error')
		idx = 1
		msg = ssc.module_log(module, 0)
		while (msg != None):
			print ('	: ' + msg.decode("utf - 8"))
			msg = ssc.module_log(module, idx)
			idx = idx + 1
		SystemExit( "Simulation Error" );
	ssc.module_free(module)
	annual_energy = ssc.data_get_number(data, b'annual_energy');
	print ('Annual AC energy in Year 1 = ', annual_energy)
	capacity_factor = ssc.data_get_number(data, b'capacity_factor');
	print ('DC capacity factor in Year 1 = ', capacity_factor)
	kwh_per_kw = ssc.data_get_number(data, b'kwh_per_kw');
	print ('Energy yield in Year 1 = ', kwh_per_kw)
	ssc.data_free(data);