# import providers, services and models
from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider
from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as ned

csr = {
'address': "192.168.212.10",
'port' : 830,
'username' : 'admin',
'password' : 'C1sc0123',
'protocol' : 'ssh'}

if __name__ == "__main__":
    """Main execution path"""

    # create NETCONF session
    provider = NetconfServiceProvider(**csr)
    # create CRUD service
    crud = CRUDService()

    # create system time object
    interface = ned.Native.Interface()

    # read system time from device
    interface = crud.read(provider, interface)

    address = interface.gigabitethernet[0].ip.address.primary
    # print system uptime
    print("Interface gig 1 address is {}/{}" .format(address.address, address.mask))

    # close NETCONF session and exit
    provider.close()
    # exit()
