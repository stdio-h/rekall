
# AUTOGENERATED File do not edit!
# File generated by the profile_tool.py 'compress' command.

from rekall import io_manager


class BuiltInProfiles(io_manager.BuiltInManager):
   data = {
 'WinXPSP2x86': {
  'metadata': {
   'Constants': 'Constants.json',
   'ProfileClass': 'WinXPSP2x86',
   'VTypes': 'vtypes.json',
  },
  'vtypes.json': {
   'LIST_ENTRY32': [8, {
    'Blink': [4, ['unsigned long']],
    'Flink': [0, ['unsigned long']],
   }],
   'LIST_ENTRY64': [16, {
   }],
   '_CLIENT_ID': [8, {
    'UniqueProcess': [0, ['pointer', ['void']]],
    'UniqueThread': [4, ['pointer', ['void']]],
   }],
   '_CMHIVE': [1180, {
    'FileFullPath': [584, ['_UNICODE_STRING']],
    'FileUserName': [592, ['_UNICODE_STRING']],
    'Hive': [0, ['_HHIVE']],
    'HiveList': [548, ['_LIST_ENTRY']],
   }],
   '_CM_KEY_BODY': [68, {
    'KeyControlBlock': [4, ['pointer', ['_CM_KEY_CONTROL_BLOCK']]],
   }],
   '_CM_KEY_CONTROL_BLOCK': [72, {
    'NameBlock': [28, ['pointer', ['_CM_NAME_CONTROL_BLOCK']]],
    'ParentKcb': [24, ['pointer', ['_CM_KEY_CONTROL_BLOCK']]],
   }],
   '_CM_KEY_INDEX': [8, {
    'Count': [2, ['unsigned short']],
    'List': [4, ['array', 1, ['unsigned long']]],
    'Signature': [0, ['unsigned short']],
   }],
   '_CM_KEY_NODE': [80, {
    'Flags': [2, ['unsigned short']],
    'LastWriteTime': [4, ['_LARGE_INTEGER']],
    'Signature': [0, ['unsigned short']],
    'SubKeyCounts': [20, ['array', 2, ['unsigned long']]],
    'SubKeyLists': [28, ['array', 2, ['unsigned long']]],
   }],
   '_CM_NAME_CONTROL_BLOCK': [16, {
    'Name': [14, ['array', 1, ['unsigned short']]],
    'NameLength': [12, ['unsigned short']],
   }],
   '_CONTROL_AREA': [48, {
    'DereferenceList': [4, ['_LIST_ENTRY']],
    'FilePointer': [36, ['pointer', ['_FILE_OBJECT']]],
    'NumberOfMappedViews': [20, ['unsigned long']],
    'NumberOfPfnReferences': [16, ['unsigned long']],
    'NumberOfSectionReferences': [12, ['unsigned long']],
    'NumberOfUserReferences': [28, ['unsigned long']],
    'Segment': [0, ['pointer', ['_SEGMENT']]],
    'WaitingForDeletion': [40, ['pointer', ['_EVENT_COUNTER']]],
    'u': [32, ['__unnamed_1224']],
   }],
   '_DBGKD_GET_VERSION64': [40, {
    'KernBase': [16, ['unsigned long long']],
    'MajorVersion': [0, ['unsigned short']],
    'MinorVersion': [2, ['unsigned short']],
    'PsLoadedModuleList': [24, ['unsigned long long']],
   }],
   '_DEVICE_OBJECT': [184, {
    'AttachedDevice': [16, ['pointer', ['_DEVICE_OBJECT']]],
    'DeviceType': [44, ['unsigned long']],
    'DriverObject': [8, ['pointer', ['_DRIVER_OBJECT']]],
    'NextDevice': [12, ['pointer', ['_DEVICE_OBJECT']]],
   }],
   '_DISPATCHER_HEADER': [16, {
    'SignalState': [4, ['long']],
    'Type': [0, ['unsigned char']],
   }],
   '_DRIVER_EXTENSION': [28, {
    'ServiceKeyName': [12, ['_UNICODE_STRING']],
   }],
   '_DRIVER_OBJECT': [168, {
    'DeviceObject': [4, ['pointer', ['_DEVICE_OBJECT']]],
    'DriverName': [28, ['_UNICODE_STRING']],
    'DriverSize': [16, ['unsigned long']],
    'DriverStart': [12, ['pointer', ['void']]],
    'DriverStartIo': [48, ['pointer', ['void']]],
    'MajorFunction': [56, ['array', 28, ['pointer', ['void']]]],
   }],
   '_DUAL': [220, {
    'Length': [0, ['unsigned long']],
    'Map': [4, ['pointer', ['_HMAP_DIRECTORY']]],
   }],
   '_EPROCESS': [608, {
    'ActiveProcessLinks': [136, ['_LIST_ENTRY']],
    'ActiveThreads': [416, ['unsigned long']],
    'AddressCreationLock': [240, ['_FAST_MUTEX']],
    'AddressSpaceInitialized': [584, ['BitField', {
     'end_bit': 12,
     'native_type': 'unsigned long',
     'start_bit': 10,
    }]],
    'AweInfo': [496, ['pointer', ['void']]],
    'BreakOnTermination': [584, ['BitField', {
     'end_bit': 14,
     'native_type': 'unsigned long',
     'start_bit': 13,
    }]],
    'CloneRoot': [292, ['pointer', ['void']]],
    'CommitCharge': [168, ['unsigned long']],
    'CommitChargeLimit': [488, ['unsigned long']],
    'CommitChargePeak': [492, ['unsigned long']],
    'Cookie': [600, ['unsigned long']],
    'CreateReported': [584, ['BitField', {
     'end_bit': 1,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
    'CreateTime': [112, ['_LARGE_INTEGER']],
    'DebugPort': [188, ['pointer', ['void']]],
    'DefaultHardErrorProcessing': [424, ['unsigned long']],
    'DeviceMap': [348, ['pointer', ['void']]],
    'ExceptionPort': [192, ['pointer', ['void']]],
    'ExitStatus': [588, ['long']],
    'ExitTime': [120, ['_LARGE_INTEGER']],
    'Filler': [360, ['unsigned long long']],
    'Flags': [584, ['unsigned long']],
    'ForkFailed': [584, ['BitField', {
     'end_bit': 9,
     'native_type': 'unsigned long',
     'start_bit': 8,
    }]],
    'ForkInProgress': [276, ['pointer', ['_ETHREAD']]],
    'GrantedAccess': [420, ['unsigned long']],
    'HardwareTrigger': [280, ['unsigned long']],
    'HasAddressSpace': [584, ['BitField', {
     'end_bit': 19,
     'native_type': 'unsigned long',
     'start_bit': 18,
    }]],
    'HasPhysicalVad': [584, ['BitField', {
     'end_bit': 10,
     'native_type': 'unsigned long',
     'start_bit': 9,
    }]],
    'HyperSpaceLock': [272, ['unsigned long']],
    'ImageFileName': [372, ['array', 16, ['unsigned char']]],
    'InheritedFromUniqueProcessId': [332, ['pointer', ['void']]],
    'InjectInpageErrors': [584, ['BitField', {
     'end_bit': 21,
     'native_type': 'unsigned long',
     'start_bit': 20,
    }]],
    'Job': [308, ['pointer', ['_EJOB']]],
    'JobLinks': [388, ['_LIST_ENTRY']],
    'JobStatus': [580, ['unsigned long']],
    'LastFaultCount': [568, ['unsigned long']],
    'LastThreadExitStatus': [428, ['long']],
    'LaunchPrefetched': [584, ['BitField', {
     'end_bit': 20,
     'native_type': 'unsigned long',
     'start_bit': 19,
    }]],
    'LdtInformation': [336, ['pointer', ['void']]],
    'LockedPagesList': [396, ['pointer', ['void']]],
    'ModifiedPageCount': [572, ['unsigned long']],
    'NextPageColor': [592, ['unsigned short']],
    'NoDebugInherit': [584, ['BitField', {
     'end_bit': 2,
     'native_type': 'unsigned long',
     'start_bit': 1,
    }]],
    'NumberOfLockedPages': [300, ['unsigned long']],
    'NumberOfPrivatePages': [296, ['unsigned long']],
    'NumberOfVads': [576, ['unsigned long']],
    'ObjectTable': [196, ['pointer', ['_HANDLE_TABLE']]],
    'OtherOperationCount': [456, ['_LARGE_INTEGER']],
    'OtherTransferCount': [480, ['_LARGE_INTEGER']],
    'OutswapEnabled': [584, ['BitField', {
     'end_bit': 7,
     'native_type': 'unsigned long',
     'start_bit': 6,
    }]],
    'Outswapped': [584, ['BitField', {
     'end_bit': 8,
     'native_type': 'unsigned long',
     'start_bit': 7,
    }]],
    'OverrideAddressSpace': [584, ['BitField', {
     'end_bit': 18,
     'native_type': 'unsigned long',
     'start_bit': 17,
    }]],
    'PaeTop': [412, ['pointer', ['void']]],
    'PageDirectoryPte': [360, ['_HARDWARE_PTE']],
    'Pcb': [0, ['_KPROCESS']],
    'PeakVirtualSize': [172, ['unsigned long']],
    'Peb': [432, ['pointer', ['_PEB']]],
    'PhysicalVadList': [352, ['_LIST_ENTRY']],
    'PrefetchTrace': [436, ['_EX_FAST_REF']],
    'PriorityClass': [596, ['unsigned char']],
    'ProcessDelete': [584, ['BitField', {
     'end_bit': 4,
     'native_type': 'unsigned long',
     'start_bit': 3,
    }]],
    'ProcessExiting': [584, ['BitField', {
     'end_bit': 3,
     'native_type': 'unsigned long',
     'start_bit': 2,
    }]],
    'ProcessInSession': [584, ['BitField', {
     'end_bit': 17,
     'native_type': 'unsigned long',
     'start_bit': 16,
    }]],
    'ProcessLock': [108, ['_EX_PUSH_LOCK']],
    'QuotaBlock': [320, ['pointer', ['_EPROCESS_QUOTA_BLOCK']]],
    'QuotaPeak': [156, ['array', 3, ['unsigned long']]],
    'QuotaUsage': [144, ['array', 3, ['unsigned long']]],
    'ReadOperationCount': [440, ['_LARGE_INTEGER']],
    'ReadTransferCount': [464, ['_LARGE_INTEGER']],
    'RundownProtect': [128, ['_EX_RUNDOWN_REF']],
    'SeAuditProcessCreationInfo': [500, ['_SE_AUDIT_PROCESS_CREATION_INFO']],
    'SectionBaseAddress': [316, ['pointer', ['void']]],
    'SectionObject': [312, ['pointer', ['void']]],
    'SecurityPort': [408, ['pointer', ['void']]],
    'Session': [368, ['pointer', ['void']]],
    'SessionCreationUnderway': [584, ['BitField', {
     'end_bit': 15,
     'native_type': 'unsigned long',
     'start_bit': 14,
    }]],
    'SessionProcessLinks': [180, ['_LIST_ENTRY']],
    'SetTimerResolution': [584, ['BitField', {
     'end_bit': 13,
     'native_type': 'unsigned long',
     'start_bit': 12,
    }]],
    'SubSystemMajorVersion': [595, ['unsigned char']],
    'SubSystemMinorVersion': [594, ['unsigned char']],
    'SubSystemVersion': [594, ['unsigned short']],
    'ThreadListHead': [400, ['_LIST_ENTRY']],
    'Token': [200, ['_EX_FAST_REF']],
    'UniqueProcessId': [132, ['pointer', ['void']]],
    'Unused': [584, ['BitField', {
     'end_bit': 30,
     'native_type': 'unsigned long',
     'start_bit': 25,
    }]],
    'Unused1': [584, ['BitField', {
     'end_bit': 31,
     'native_type': 'unsigned long',
     'start_bit': 30,
    }]],
    'Unused2': [584, ['BitField', {
     'end_bit': 32,
     'native_type': 'unsigned long',
     'start_bit': 31,
    }]],
    'Unused3': [584, ['BitField', {
     'end_bit': 23,
     'native_type': 'unsigned long',
     'start_bit': 22,
    }]],
    'Unused4': [584, ['BitField', {
     'end_bit': 24,
     'native_type': 'unsigned long',
     'start_bit': 23,
    }]],
    'VadFreeHint': [340, ['pointer', ['void']]],
    'VadHint': [288, ['pointer', ['void']]],
    'VadRoot': [284, ['pointer', ['void']]],
    'VdmAllowed': [584, ['BitField', {
     'end_bit': 25,
     'native_type': 'unsigned long',
     'start_bit': 24,
    }]],
    'VdmObjects': [344, ['pointer', ['void']]],
    'VirtualSize': [176, ['unsigned long']],
    'Vm': [504, ['_MMSUPPORT']],
    'VmDeleted': [584, ['BitField', {
     'end_bit': 6,
     'native_type': 'unsigned long',
     'start_bit': 5,
    }]],
    'VmTopDown': [584, ['BitField', {
     'end_bit': 22,
     'native_type': 'unsigned long',
     'start_bit': 21,
    }]],
    'Win32Process': [304, ['pointer', ['void']]],
    'Win32WindowStation': [328, ['pointer', ['void']]],
    'WorkingSetAcquiredUnsafe': [597, ['unsigned char']],
    'WorkingSetLock': [204, ['_FAST_MUTEX']],
    'WorkingSetPage': [236, ['unsigned long']],
    'WorkingSetWatch': [324, ['pointer', ['_PAGEFAULT_HISTORY']]],
    'Wow64SplitPages': [584, ['BitField', {
     'end_bit': 5,
     'native_type': 'unsigned long',
     'start_bit': 4,
    }]],
    'WriteOperationCount': [448, ['_LARGE_INTEGER']],
    'WriteTransferCount': [472, ['_LARGE_INTEGER']],
    'WriteWatch': [584, ['BitField', {
     'end_bit': 16,
     'native_type': 'unsigned long',
     'start_bit': 15,
    }]],
   }],
   '_ETHREAD': [600, {
    'Cid': [492, ['_CLIENT_ID']],
    'CreateTime': [448, ['_LARGE_INTEGER']],
    'ExitTime': [456, ['_LARGE_INTEGER']],
    'KeyedWaitSemaphore': [500, ['_KSEMAPHORE']],
    'StartAddress': [548, ['pointer', ['void']]],
    'Tcb': [0, ['_KTHREAD']],
    'ThreadsProcess': [544, ['pointer', ['_EPROCESS']]],
   }],
   '_EX_FAST_REF': [4, {
    'Object': [0, ['pointer', ['void']]],
   }],
   '_EX_PUSH_LOCK': [4, {
   }],
   '_EX_RUNDOWN_REF': [4, {
   }],
   '_FAST_MUTEX': [32, {
   }],
   '_FILE_OBJECT': [112, {
    'DeleteAccess': [40, ['unsigned char']],
    'DeviceObject': [4, ['pointer', ['_DEVICE_OBJECT']]],
    'FileName': [48, ['_UNICODE_STRING']],
    'ReadAccess': [38, ['unsigned char']],
    'SharedDelete': [43, ['unsigned char']],
    'SharedRead': [41, ['unsigned char']],
    'SharedWrite': [42, ['unsigned char']],
    'WriteAccess': [39, ['unsigned char']],
   }],
   '_HANDLE_TABLE': [68, {
    'HandleCount': [60, ['long']],
    'HandleTableList': [28, ['_LIST_ENTRY']],
    'TableCode': [0, ['unsigned long']],
   }],
   '_HANDLE_TABLE_ENTRY': [8, {
    'GrantedAccess': [4, ['unsigned long']],
    'Object': [0, ['pointer', ['void']]],
   }],
   '_HARDWARE_PTE': [4, {
   }],
   '_HHIVE': [528, {
    'BaseBlock': [36, ['pointer', ['_HBASE_BLOCK']]],
    'Flat': [64, ['unsigned char']],
    'Signature': [0, ['unsigned long']],
    'Storage': [88, ['array', 2, ['_DUAL']]],
   }],
   '_HMAP_DIRECTORY': [4096, {
    'Directory': [0, ['array', 1024, ['pointer', ['_HMAP_TABLE']]]],
   }],
   '_HMAP_ENTRY': [16, {
    'BlockAddress': [0, ['unsigned long']],
   }],
   '_HMAP_TABLE': [8192, {
    'Table': [0, ['array', 512, ['_HMAP_ENTRY']]],
   }],
   '_IMAGE_DATA_DIRECTORY': [8, {
    'Size': [4, ['unsigned long']],
    'VirtualAddress': [0, ['unsigned long']],
   }],
   '_IMAGE_DOS_HEADER': [64, {
    'e_lfanew': [60, ['long']],
    'e_magic': [0, ['unsigned short']],
   }],
   '_IMAGE_NT_HEADERS': [248, {
    'OptionalHeader': [24, ['_IMAGE_OPTIONAL_HEADER']],
    'Signature': [0, ['unsigned long']],
   }],
   '_IMAGE_OPTIONAL_HEADER': [224, {
    'DataDirectory': [96, ['array', 16, ['_IMAGE_DATA_DIRECTORY']]],
    'Magic': [0, ['unsigned short']],
    'MajorOperatingSystemVersion': [40, ['unsigned short']],
    'MinorOperatingSystemVersion': [42, ['unsigned short']],
    'SizeOfImage': [56, ['unsigned long']],
   }],
   '_KAPC_STATE': [24, {
    'Process': [16, ['pointer', ['_KPROCESS']]],
   }],
   '_KDPC': [32, {
    'DeferredRoutine': [12, ['pointer', ['void']]],
   }],
   '_KMUTANT': [32, {
    'Header': [0, ['_DISPATCHER_HEADER']],
    'OwnerThread': [24, ['pointer', ['_KTHREAD']]],
   }],
   '_KPCR': [3440, {
    'Prcb': [32, ['pointer', ['_KPRCB']]],
    'PrcbData': [288, ['_KPRCB']],
   }],
   '_KPRCB': [3152, {
    'Number': [16, ['unsigned char']],
   }],
   '_KPROCESS': [108, {
    'DirectoryTableBase': [24, ['array', 2, ['unsigned long']]],
   }],
   '_KSEMAPHORE': [20, {
    'Header': [0, ['_DISPATCHER_HEADER']],
   }],
   '_KTHREAD': [448, {
    'ApcState': [52, ['_KAPC_STATE']],
    'SuspendSemaphore': [412, ['_KSEMAPHORE']],
   }],
   '_KTIMER': [40, {
    'Dpc': [32, ['pointer', ['_KDPC']]],
    'DueTime': [16, ['_ULARGE_INTEGER']],
    'Header': [0, ['_DISPATCHER_HEADER']],
    'Period': [36, ['long']],
    'TimerListEntry': [24, ['_LIST_ENTRY']],
   }],
   '_LARGE_INTEGER': [8, {
   }],
   '_LDR_DATA_TABLE_ENTRY': [80, {
    'BaseDllName': [44, ['_UNICODE_STRING']],
    'DllBase': [24, ['pointer', ['void']]],
    'FullDllName': [36, ['_UNICODE_STRING']],
    'InInitializationOrderLinks': [16, ['_LIST_ENTRY']],
    'InLoadOrderLinks': [0, ['_LIST_ENTRY']],
    'InMemoryOrderLinks': [8, ['_LIST_ENTRY']],
    'SizeOfImage': [32, ['unsigned long']],
   }],
   '_LIST_ENTRY': [8, {
    'Blink': [4, ['pointer', ['_LIST_ENTRY']]],
    'Flink': [0, ['pointer', ['_LIST_ENTRY']]],
   }],
   '_MMPFN': [24, {
    'PteAddress': [4, ['pointer', ['_MMPTE']]],
    'u1': [0, ['__unnamed_179d']],
    'u3': [12, ['__unnamed_17a4']],
    'u4': [20, ['__unnamed_17aa']],
   }],
   '_MMPFNENTRY': [4, {
    'PageLocation': [0, ['BitField', {
     'end_bit': 11,
     'native_type': 'unsigned long',
     'start_bit': 8,
    }]],
   }],
   '_MMSECTION_FLAGS': [4, {
    'Accessed': [0, ['BitField', {
     'end_bit': 28,
     'native_type': 'unsigned long',
     'start_bit': 27,
    }]],
    'Based': [0, ['BitField', {
     'end_bit': 7,
     'native_type': 'unsigned long',
     'start_bit': 6,
    }]],
    'BeingCreated': [0, ['BitField', {
     'end_bit': 2,
     'native_type': 'unsigned long',
     'start_bit': 1,
    }]],
    'BeingDeleted': [0, ['BitField', {
     'end_bit': 1,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
    'BeingPurged': [0, ['BitField', {
     'end_bit': 3,
     'native_type': 'unsigned long',
     'start_bit': 2,
    }]],
    'CollidedFlush': [0, ['BitField', {
     'end_bit': 23,
     'native_type': 'unsigned long',
     'start_bit': 22,
    }]],
    'Commit': [0, ['BitField', {
     'end_bit': 14,
     'native_type': 'unsigned long',
     'start_bit': 13,
    }]],
    'CopyOnWrite': [0, ['BitField', {
     'end_bit': 12,
     'native_type': 'unsigned long',
     'start_bit': 11,
    }]],
    'DebugSymbolsLoaded': [0, ['BitField', {
     'end_bit': 21,
     'native_type': 'unsigned long',
     'start_bit': 20,
    }]],
    'DeleteOnClose': [0, ['BitField', {
     'end_bit': 19,
     'native_type': 'unsigned long',
     'start_bit': 18,
    }]],
    'FailAllIo': [0, ['BitField', {
     'end_bit': 5,
     'native_type': 'unsigned long',
     'start_bit': 4,
    }]],
    'File': [0, ['BitField', {
     'end_bit': 8,
     'native_type': 'unsigned long',
     'start_bit': 7,
    }]],
    'FilePointerNull': [0, ['BitField', {
     'end_bit': 20,
     'native_type': 'unsigned long',
     'start_bit': 19,
    }]],
    'FloppyMedia': [0, ['BitField', {
     'end_bit': 15,
     'native_type': 'unsigned long',
     'start_bit': 14,
    }]],
    'GlobalMemory': [0, ['BitField', {
     'end_bit': 18,
     'native_type': 'unsigned long',
     'start_bit': 17,
    }]],
    'GlobalOnlyPerSession': [0, ['BitField', {
     'end_bit': 29,
     'native_type': 'unsigned long',
     'start_bit': 28,
    }]],
    'HadUserReference': [0, ['BitField', {
     'end_bit': 25,
     'native_type': 'unsigned long',
     'start_bit': 24,
    }]],
    'Image': [0, ['BitField', {
     'end_bit': 6,
     'native_type': 'unsigned long',
     'start_bit': 5,
    }]],
    'ImageMappedInSystemSpace': [0, ['BitField', {
     'end_bit': 26,
     'native_type': 'unsigned long',
     'start_bit': 25,
    }]],
    'Networked': [0, ['BitField', {
     'end_bit': 9,
     'native_type': 'unsigned long',
     'start_bit': 8,
    }]],
    'NoCache': [0, ['BitField', {
     'end_bit': 10,
     'native_type': 'unsigned long',
     'start_bit': 9,
    }]],
    'NoChange': [0, ['BitField', {
     'end_bit': 24,
     'native_type': 'unsigned long',
     'start_bit': 23,
    }]],
    'NoModifiedWriting': [0, ['BitField', {
     'end_bit': 4,
     'native_type': 'unsigned long',
     'start_bit': 3,
    }]],
    'PhysicalMemory': [0, ['BitField', {
     'end_bit': 11,
     'native_type': 'unsigned long',
     'start_bit': 10,
    }]],
    'Reserve': [0, ['BitField', {
     'end_bit': 13,
     'native_type': 'unsigned long',
     'start_bit': 12,
    }]],
    'Rom': [0, ['BitField', {
     'end_bit': 30,
     'native_type': 'unsigned long',
     'start_bit': 29,
    }]],
    'SetMappedFileIoComplete': [0, ['BitField', {
     'end_bit': 22,
     'native_type': 'unsigned long',
     'start_bit': 21,
    }]],
    'UserReference': [0, ['BitField', {
     'end_bit': 17,
     'native_type': 'unsigned long',
     'start_bit': 16,
    }]],
    'UserWritable': [0, ['BitField', {
     'end_bit': 27,
     'native_type': 'unsigned long',
     'start_bit': 26,
    }]],
    'WasPurged': [0, ['BitField', {
     'end_bit': 16,
     'native_type': 'unsigned long',
     'start_bit': 15,
    }]],
    'filler': [0, ['BitField', {
     'end_bit': 32,
     'native_type': 'unsigned long',
     'start_bit': 30,
    }]],
   }],
   '_MMSUPPORT': [64, {
   }],
   '_MMVAD': [40, {
    'ControlArea': [24, ['pointer', ['_CONTROL_AREA']]],
    'EndingVpn': [4, ['unsigned long']],
    'FirstPrototypePte': [28, ['pointer', ['_MMPTE']]],
    'LastContiguousPte': [32, ['pointer', ['_MMPTE']]],
    'LeftChild': [12, ['pointer', ['_MMVAD']]],
    'RightChild': [16, ['pointer', ['_MMVAD']]],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_144c']],
    'u2': [36, ['__unnamed_144f']],
   }],
   '_MMVAD_FLAGS': [4, {
    'CommitCharge': [0, ['BitField', {
     'end_bit': 19,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
    'ImageMap': [0, ['BitField', {
     'end_bit': 21,
     'native_type': 'unsigned long',
     'start_bit': 20,
    }]],
    'LargePages': [0, ['BitField', {
     'end_bit': 30,
     'native_type': 'unsigned long',
     'start_bit': 29,
    }]],
    'MemCommit': [0, ['BitField', {
     'end_bit': 31,
     'native_type': 'unsigned long',
     'start_bit': 30,
    }]],
    'NoChange': [0, ['BitField', {
     'end_bit': 23,
     'native_type': 'unsigned long',
     'start_bit': 22,
    }]],
    'PhysicalMapping': [0, ['BitField', {
     'end_bit': 20,
     'native_type': 'unsigned long',
     'start_bit': 19,
    }]],
    'PrivateMemory': [0, ['BitField', {
     'end_bit': 32,
     'native_type': 'unsigned long',
     'start_bit': 31,
    }]],
    'Protection': [0, ['BitField', {
     'end_bit': 29,
     'native_type': 'unsigned long',
     'start_bit': 24,
    }]],
    'UserPhysicalPages': [0, ['BitField', {
     'end_bit': 22,
     'native_type': 'unsigned long',
     'start_bit': 21,
    }]],
    'WriteWatch': [0, ['BitField', {
     'end_bit': 24,
     'native_type': 'unsigned long',
     'start_bit': 23,
    }]],
   }],
   '_MMVAD_FLAGS2': [4, {
    'CopyOnWrite': [0, ['BitField', {
     'end_bit': 32,
     'native_type': 'unsigned long',
     'start_bit': 31,
    }]],
    'ExtendableFile': [0, ['BitField', {
     'end_bit': 30,
     'native_type': 'unsigned long',
     'start_bit': 29,
    }]],
    'FileOffset': [0, ['BitField', {
     'end_bit': 24,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
    'Inherit': [0, ['BitField', {
     'end_bit': 31,
     'native_type': 'unsigned long',
     'start_bit': 30,
    }]],
    'LongVad': [0, ['BitField', {
     'end_bit': 29,
     'native_type': 'unsigned long',
     'start_bit': 28,
    }]],
    'MultipleSecured': [0, ['BitField', {
     'end_bit': 27,
     'native_type': 'unsigned long',
     'start_bit': 26,
    }]],
    'OneSecured': [0, ['BitField', {
     'end_bit': 26,
     'native_type': 'unsigned long',
     'start_bit': 25,
    }]],
    'ReadOnly': [0, ['BitField', {
     'end_bit': 28,
     'native_type': 'unsigned long',
     'start_bit': 27,
    }]],
    'SecNoChange': [0, ['BitField', {
     'end_bit': 25,
     'native_type': 'unsigned long',
     'start_bit': 24,
    }]],
   }],
   '_MMVAD_LONG': [52, {
    'ControlArea': [24, ['pointer', ['_CONTROL_AREA']]],
    'EndingVpn': [4, ['unsigned long']],
    'FirstPrototypePte': [28, ['pointer', ['_MMPTE']]],
    'LastContiguousPte': [32, ['pointer', ['_MMPTE']]],
    'LeftChild': [12, ['pointer', ['_MMVAD']]],
    'RightChild': [16, ['pointer', ['_MMVAD']]],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_144c']],
    'u2': [36, ['__unnamed_144f']],
   }],
   '_MMVAD_SHORT': [24, {
    'EndingVpn': [4, ['unsigned long']],
    'LeftChild': [12, ['pointer', ['_MMVAD']]],
    'RightChild': [16, ['pointer', ['_MMVAD']]],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_144c']],
   }],
   '_MM_SESSION_SPACE': [4728, {
    'ImageList': [156, ['_LIST_ENTRY']],
    'PagedPoolEnd': [104, ['pointer', ['void']]],
    'PagedPoolStart': [100, ['pointer', ['void']]],
    'ProcessList': [20, ['_LIST_ENTRY']],
    'SessionId': [8, ['unsigned long']],
   }],
   '_OBJECT_HEADER': [32, {
    'Body': [24, ['_QUAD']],
    'HandleCount': [4, ['long']],
    'NameInfoOffset': [12, ['unsigned char']],
    'PointerCount': [0, ['long']],
    'Type': [8, ['pointer', ['_OBJECT_TYPE']]],
   }],
   '_OBJECT_HEADER_NAME_INFO': [16, {
    'Name': [4, ['_UNICODE_STRING']],
   }],
   '_OBJECT_SYMBOLIC_LINK': [32, {
    'CreationTime': [0, ['_LARGE_INTEGER']],
    'LinkTarget': [8, ['_UNICODE_STRING']],
   }],
   '_OBJECT_TYPE': [400, {
    'Name': [64, ['_UNICODE_STRING']],
   }],
   '_PEB': [528, {
    'CSDVersion': [496, ['_UNICODE_STRING']],
    'ImageBaseAddress': [8, ['pointer', ['void']]],
    'Ldr': [12, ['pointer', ['_PEB_LDR_DATA']]],
    'ProcessParameters': [16, ['pointer', ['_RTL_USER_PROCESS_PARAMETERS']]],
   }],
   '_PEB_LDR_DATA': [40, {
    'InInitializationOrderModuleList': [28, ['_LIST_ENTRY']],
    'InLoadOrderModuleList': [12, ['_LIST_ENTRY']],
    'InMemoryOrderModuleList': [20, ['_LIST_ENTRY']],
   }],
   '_POOL_HEADER': [8, {
    'BlockSize': [2, ['BitField', {
     'end_bit': 9,
     'native_type': 'unsigned short',
     'start_bit': 0,
    }]],
    'PoolIndex': [0, ['BitField', {
     'end_bit': 16,
     'native_type': 'unsigned short',
     'start_bit': 9,
    }]],
    'PoolTag': [4, ['unsigned long']],
    'PoolType': [2, ['BitField', {
     'end_bit': 16,
     'native_type': 'unsigned short',
     'start_bit': 9,
    }]],
   }],
   '_QUAD': [8, {
   }],
   '_RTL_ATOM_TABLE': [68, {
    'Buckets': [64, ['array', 1, ['pointer', ['_RTL_ATOM_TABLE_ENTRY']]]],
    'Signature': [0, ['unsigned long']],
   }],
   '_RTL_ATOM_TABLE_ENTRY': [16, {
    'Atom': [6, ['unsigned short']],
    'Flags': [10, ['unsigned char']],
    'HandleIndex': [4, ['unsigned short']],
    'HashLink': [0, ['pointer', ['_RTL_ATOM_TABLE_ENTRY']]],
    'Name': [12, ['array', 1, ['unsigned short']]],
    'NameLength': [11, ['unsigned char']],
    'ReferenceCount': [8, ['unsigned short']],
   }],
   '_RTL_USER_PROCESS_PARAMETERS': [656, {
    'CommandLine': [64, ['_UNICODE_STRING']],
    'Environment': [72, ['pointer', ['void']]],
   }],
   '_SE_AUDIT_PROCESS_CREATION_INFO': [4, {
   }],
   '_SID': [12, {
    'IdentifierAuthority': [2, ['_SID_IDENTIFIER_AUTHORITY']],
    'Revision': [0, ['unsigned char']],
    'SubAuthority': [8, ['array', 1, ['unsigned long']]],
    'SubAuthorityCount': [1, ['unsigned char']],
   }],
   '_SID_AND_ATTRIBUTES': [8, {
    'Sid': [0, ['pointer', ['void']]],
   }],
   '_SID_IDENTIFIER_AUTHORITY': [6, {
    'Value': [0, ['array', 6, ['unsigned char']]],
   }],
   '_TOKEN': [168, {
    'UserAndGroupCount': [76, ['unsigned long']],
    'UserAndGroups': [104, ['pointer', ['_SID_AND_ATTRIBUTES']]],
   }],
   '_ULARGE_INTEGER': [8, {
    'QuadPart': [0, ['unsigned long long']],
   }],
   '_UNICODE_STRING': [8, {
    'Buffer': [4, ['pointer', ['unsigned short']]],
    'Length': [0, ['unsigned short']],
   }],
   '__unnamed_1224': [4, {
    'Flags': [0, ['_MMSECTION_FLAGS']],
   }],
   '__unnamed_144c': [4, {
    'VadFlags': [0, ['_MMVAD_FLAGS']],
   }],
   '__unnamed_144f': [4, {
    'VadFlags2': [0, ['_MMVAD_FLAGS2']],
   }],
   '__unnamed_179d': [4, {
    'Flink': [0, ['unsigned long']],
   }],
   '__unnamed_17a4': [4, {
    'e1': [0, ['_MMPFNENTRY']],
   }],
   '__unnamed_17aa': [4, {
    'PteFrame': [0, ['BitField', {
     'end_bit': 26,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
   }],
  },
 },
 'WinXPSP3x86': {
  'metadata': {
   'Constants': 'Constants.json',
   'ProfileClass': 'WinXPSP3x86',
   'VTypes': 'vtypes.json',
  },
  'vtypes.json': {
   'LIST_ENTRY32': [8, {
    'Blink': [4, ['unsigned long']],
    'Flink': [0, ['unsigned long']],
   }],
   'LIST_ENTRY64': [16, {
   }],
   '_CONTROL_AREA': [48, {
    'FilePointer': [36, ['pointer', ['_FILE_OBJECT']]],
   }],
   '_EPROCESS': [608, {
    'ActiveProcessLinks': [136, ['_LIST_ENTRY']],
    'ActiveThreads': [416, ['unsigned long']],
    'CreateTime': [112, ['_LARGE_INTEGER']],
    'ExitTime': [120, ['_LARGE_INTEGER']],
    'ImageFileName': [372, ['array', 16, ['unsigned char']]],
    'InheritedFromUniqueProcessId': [332, ['pointer', ['void']]],
    'ObjectTable': [196, ['pointer', ['_HANDLE_TABLE']]],
    'Pcb': [0, ['_KPROCESS']],
    'Session': [368, ['pointer', ['void']]],
    'ThreadListHead': [400, ['_LIST_ENTRY']],
    'UniqueProcessId': [132, ['pointer', ['void']]],
    'VadRoot': [284, ['pointer', ['void']]],
   }],
   '_FILE_OBJECT': [112, {
    'FileName': [48, ['_UNICODE_STRING']],
   }],
   '_HANDLE_TABLE': [68, {
    'HandleCount': [60, ['long']],
   }],
   '_KPROCESS': [108, {
    'DirectoryTableBase': [24, ['array', 2, ['unsigned long']]],
   }],
   '_LIST_ENTRY': [8, {
    'Blink': [4, ['pointer', ['_LIST_ENTRY']]],
    'Flink': [0, ['pointer', ['_LIST_ENTRY']]],
   }],
   '_MMVAD': [40, {
    'ControlArea': [24, ['pointer', ['_CONTROL_AREA']]],
    'EndingVpn': [4, ['unsigned long']],
    'LeftChild': [12, ['pointer', ['_MMVAD']]],
    'RightChild': [16, ['pointer', ['_MMVAD']]],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_1492']],
   }],
   '_MMVAD_FLAGS': [4, {
    'CommitCharge': [0, ['BitField', {
     'end_bit': 19,
     'native_type': 'unsigned long',
     'start_bit': 0,
    }]],
    'PrivateMemory': [0, ['BitField', {
     'end_bit': 32,
     'native_type': 'unsigned long',
     'start_bit': 31,
    }]],
    'Protection': [0, ['BitField', {
     'end_bit': 29,
     'native_type': 'unsigned long',
     'start_bit': 24,
    }]],
   }],
   '_MMVAD_LONG': [52, {
    'ControlArea': [24, ['pointer', ['_CONTROL_AREA']]],
    'EndingVpn': [4, ['unsigned long']],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_1492']],
   }],
   '_MMVAD_SHORT': [24, {
    'EndingVpn': [4, ['unsigned long']],
    'StartingVpn': [0, ['unsigned long']],
    'u': [20, ['__unnamed_1492']],
   }],
   '_MM_SESSION_SPACE': [4728, {
    'SessionId': [8, ['unsigned long']],
   }],
   '_UNICODE_STRING': [8, {
    'Buffer': [4, ['pointer', ['unsigned short']]],
    'Length': [0, ['unsigned short']],
   }],
   '__unnamed_1492': [4, {
    'VadFlags': [0, ['_MMVAD_FLAGS']],
   }],
  },
 },
}

