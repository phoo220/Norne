import datetime

def run(ecl_state, schedule, report_step, summary_state, actionx_callback):

    current_time = schedule.start + datetime.timedelta(seconds=summary_state.elapsed())
    
    BHP_TOP = summary_state.well_var("C-2H","WBP4")
    BHP_BOT = summary_state.well_var("C-2L","WBP4")
    DeltaP = BHP_BOT - BHP_TOP
    
    #SHUT = no cross flow
    #STOP = cross flow  
    
    if (not DeltaP <= 0 ):
        print("Bottom layer opens at {}\n".format(current_time))
        print('DeltaP-', DeltaP)
        schedule.stop_well("C-1C",report_step) 
        schedule.stop_well("C-2C",report_step) 
        schedule.stop_well("C-3C",report_step) 
        schedule.stop_well("C-4C",report_step) 
        
    if (DeltaP <= 0 ):
        print("Bottom layer closes at {}\n".format(current_time))
        print('DeltaP-', DeltaP)
        schedule.shut_well("C-1C",report_step+1)  
        schedule.shut_well("C-2C",report_step+1)
        schedule.shut_well("C-3C",report_step+1)
        schedule.shut_well("C-4C",report_step+1)    