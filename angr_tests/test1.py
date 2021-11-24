import angr

bin_path = 'E:\\CODE\\cANDcpp\\test20211008\\main.exe'

proj = angr.Project(bin_path)
state = proj.factory.entry_state()
simgr = proj.factory.simgr(state)
