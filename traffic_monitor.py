import os 
from subprocess import check_output, check_call

#variables
path = os.getcwd()
threshold = 100.0 # homex/username

class traffic_monitor():
    
    def get_traffic_percent(self):
        traffic_percent = check_output(f"app-traffic info", shell=True)
        traffic_percent = traffic_percent.decode("utf-8")
        traffic_percent = traffic_percent.split()
        traffic_percent = float(traffic_percent[18].replace("%",""))
        return traffic_percent
    
    def check_traffic_stop_apps(self, traffic_percent,threshold,torrent_client_list):
        if traffic_percent <= threshold:
            for i in torrent_client_list:
                os.system("app-{} stop".format(i))
        else:
            pass
    
    
    def check_installed_torrent_client(self):
        installed_torrent_client = ['qBittorrent','rtorrent','deluge','transmission-daemon']
        torrent_client = []
        optimize_client = []
        for i in installed_torrent_client:
            status = os.path.exists("{home_dir}/.config/{i}".format(home_dir=path,i=i))
            if status:
                optimize_client.append(i)
        
        if 'rtorrent' in optimize_client:
            torrent_client.append('rtorrent')
        if 'deluge' in optimize_client:
            torrent_client.append('deluge')
        if 'qBittorrent' in optimize_client:
            torrent_client.append('qbittorrent')
        if 'transmission-daemon' in optimize_client:
            torrent_client.append('transmission')
        return torrent_client
            
    def stop_torrent_client(self,client):
        os.system("app-{} stop".format(client))
        
traffic = traffic_monitor()
if __name__ == '__main__':
    traffic_percent = traffic.get_traffic_percent()
    torrent_client_list = traffic.check_installed_torrent_client()
    traffic.check_traffic_stop_apps(traffic_percent,threshold,torrent_client_list)
    