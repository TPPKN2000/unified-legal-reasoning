# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. - Người có quyền lợi, nghĩa vụ liên quan:
2. Ông Trần Văn Q, sinh năm 1966.
3. Địa chỉ: Số 30, tổ 10, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
4. Ông Trần Quang H1, sinh năm 1972.
5. Địa chỉ:  tổ 12, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
6. Bà Trần Thị Thúy N, sinh năm 1961.
7. Bà Trần Thị Bích Th, sinh năm 1963.
8. Ông Trần Văn T, sinh năm 1959.
9. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, Đồng Nai.
10. Ông  T  ủy  quyền  cho  ông  Trần  Quốc  H  theo  văn  bản  ủy  quyền  ngày
11. 07/3/2017.
12. 6/ Ông Trần Đình P, sinh năm 1970.
13. Địa chỉ: xã C, huyện L, tỉnh Đồng Nai.
14. Ông P ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 08/3/2017.
15. 7/ Bà Trần Thị Đan Ng, sinh năm 1953.
16. Địa chỉ: Số 45 N, phường 19, quận M, TP. Hồ Chí Minh.
17. 8/ Bà Trần Thị Lệ K, sinh năm 1974.
18. Địa chỉ: Số 19B, tổ 12, khu S, thị trấn L, huyện L, Đồng Nai.
19. 9/ Bà Nguyễn Thị Th P, sinh năm 1971.
20. Địa chỉ: tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
21. Bà P ủy quyền cho ông Trần Văn T theo văn bản ủy quyền ngày 16/10/2017.
22. 10/ Chị Trần Thị Th V, sinh năm 1992.
23. 11/  Cháu  Trần  Hạo  X,  sinh  ngày  27/10/2013.  Do  chị  V  đại  diện  theo  pháp
24. 12/ Anh Trần Văn R, sinh năm 1994.
25. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
26. 13/ Anh Hoàng Thái Th1, sinh năm 1989.
27. 14/ Chị Hồ Thị Ngọc O, sinh năm 1988.
28. Địa chỉ: Ấp 2, xã Z, huyện L, tỉnh Đồng Nai.
29. Chị O ủy quyền cho anh Hoàng Thái Th1.
30. 15/ Ngân hàng thương mại cổ phần Y.
31. Địa chỉ: 25 bis A, phường B, quận C, TP. Hồ Chí Minh.
32. Người  đại  diện  theo  pháp  luật:  Ông  Nguyễn  Hữu  D  –  chức  vụ:  Tổng  giám
33. luật.
34. đốc.
35. Người đại diện theo ủy quyền: Anh Nguyễn Hữu S – Nhân viên ngân hàng.
36. 16/ Bà Phạm Thị E, sinh năm 1979.
37. Địa chỉ: Số 390 khu 1, thị trấn L, huyện L, tỉnh Đồng Nai.
38. Bà E ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 17/11/2017.
39. (Ông Đ, ông T, ông H, ông Q, ông H1, bà N, bà Th, bà Ng, bà K, anh Th1,
40. anh S có mặt, anh R, chị V đề nghị vắng mặt).
41. NỘI DUNG VỤ ÁN:
42. -  Tại  đơn  khởi  kiện  ngày  10  tháng  02  năm  2017  và  trong  quá  trình  xét  xử,
43. nguyên đơn ông Trần Văn Đ, ông Trần Văn T trình bày:
44. Cha mẹ của hai ông là Trần Văn Q1 (Trần Văn Q1), sinh năm 1923, mất năm
45. 2007; bà Trần Thị M, sinh năm 1931, mất năm 2008. Cha mẹ của ông Q1 và bà M
46. đã mất từ lâu. Ông Q1 và bà M sinh được 15 người con, chết 04 người khi còn trẻ và
47. chưa lập gia đình, hiện giờ còn 11 người, tên là:
48. Ông Trần Văn Đ, sinh năm 1951.
49. Bà Trần Thị Đan Ng, sinh năm 1953.
50. Ông Trần Văn T, sinh năm 1959.
51. Bà Trần Thị Thúy N, sinh năm 1961.
52. Bà Trần Thị Bích Th, sinh năm 1963.
53. Ông Trần Văn T, sinh năm 1964.
54. Ông Trần Văn Q, sinh năm 1966.
55. Ông Trần Đình P, sinh năm 1970.
56. Ông Trần Quang H1, sinh năm 1972.
57. Bà Trần Thị Lệ K, sinh năm 1974.
58. Ông Trần Quốc H, sinh năm 1976.
59. Ông Q1, bà M không còn người con chung hay con riêng, con nuôi nào khác.
60. Ông Q1 và bà M để lại tài sản chung là diện tích đất 488m2 thửa đất số 101, tờ
61. bản đồ số 1 xã  A, huyện L, tỉnh Đồng Nai và tài sản gắn liền với đất. Nay là diện
62. tích đất 432,1m2 Thộc thửa 51, tờ bản đồ số 11 xã A theo bản đồ hiện trạng thửa đất
63. số 8603/2017 ngày 30/6/2017 của Văn phòng đăng ký đất đai tỉnh  Đồng Nai – chi
64. nhánh L.
65. Khi ông Q1, bà M mất thì không để lại di chúc. Tất cả anh em trong gia đình
66. có ký vào tờ thỏa thuận phân chia di sản ngày 20/7/2009 tại UBND xã A để cho ông
67. H thay mặt các anh em đứng tên quản lý, sử dụng đất nhưng không biết nội dung tờ
68. thỏa thuận là gì, vì khi ký ông H chỉ đưa cho các anh em ký vào tờ giấy trắng chứ
69. không có nội dung gì trên đó. Tuy nhiên hai ông không photo tờ giấy trắng có chữ
70. ký đó lại nên không có tài liệu để cung cấp cho Tòa án. Hai ông có nói với ông H là
71. chỉ được quản lý, sử dụng diện tích đất trên để ở và không được chuyển nhượng cho
72. người khác. Ông H cũng hứa với các anh em là chỉ ở và sẽ không chuyển nhượng.
73. Tại phiên tòa ngày 26/4/2018, hai ông thừa nhận là có biết nội dung tại tờ thỏa
74. thuận như có tại hồ sơ vụ án nhưng chỉ ký với mục đích là cho ông H đứng tên trên
75. giấy chứng nhận quyền sử dụng đất mà thôi.
76. Khi ký, tất cả các anh em đều tự nguyện, không nhầm lẫn, không bị ai lừa dối
77. hay ép buộc, đe dọa gì. Tờ thỏa thuận phân chia di sản ngày 20/7/2009 cũng không
78. phải là giả tạo để che giấu một giao dịch nào khác.
79. Hiện  nay  trên  phần  đất  đó  có  bà  Trần  Thị  Bích  Th  (độc  thân),  bà  Trần  Thị
80. Thúy N (độc thân), ông Trần Văn T (độc thân) và ông Trần Quốc H, các con của ông
81. T là Trần Văn R (độc thân), Trần Thị Th V (độc thân), con của chị V là cháu Trần
82. Hạo X đang sinh sống. Trước đây vợ cV ông T có sống trên đất này nhưng  vợ cV
83. ông đã chuyển chỗ ở sang nhà kế bên đất đang tranh chấp, còn phòng ở do ông sử
84. dụng trước đây thì hiện nay con trai là Trần Văn R đang sử dụng, còn con gái tên V
85. và cháu X thì ở chung phòng với bà Th. Trong thời gian ở trên đất thì ông T có sửa
86. chữa  nhà  nhưng  ông  không  yêu  cầu  gì,  không  yêu  cầu  giải  quyết  chi  phí  cho  việc
87. bảo quản di sản hay yêu cầu nào khác. Việc ông H thế chấp phần đất trên để vay vốn
88. ngân hàng thì hai ông không hề biết.
89. Nay ông Đ, ông T yêu cầu Tòa án phân chia di sản thừa kế của ông Q1 và bà
90. M để lại là diện tích đất 432,1m2 thửa số 51, tờ bản đồ số 11 xã  A, huyện L và tài
91. sản  gắn  liền  với  đất,  trị  giá  1.692.700.000  đồng  theo  Chứng  thư  thẩm  định  giá  số
92. 2103/TĐG-CT ngày 31/8/2017 của Công ty cổ phần thẩm định giá Đồng Nai thành
93. 11 phần bằng nhau theo giá trị. Yêu cầu để ông T nhận di sản bằng hiện vật là nhà
94. đất và thanh toán giá trị cho 10 người còn lại, mỗi người được hưởng 1/10 giá trị của
95. tài sản, tương đương với số tiền là 169.270.000 đồng. Ông Đ, ông T không yêu cầu
96. thẩm định giá lại tài sản tranh chấp, đề nghị Tòa án áp dụng chứng thư thẩm định giá
97. có tại hồ sơ vụ án để giải quyết.
98. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
99. 23/01/2017 giữa ông Trần Quốc H, bà Phạm Thị E với ông H1 Thái Th1, chị Hồ Thị
100. Ngọc O thì ông Đ, ông T không đồng ý. Tuy nhiên, hai ông không có yêu cầu gì đối
101. với hợp đồng này, việc này tự ông H và ông Th1 giải quyết. Ngoài ra, ông Đ, ông T
102. không có ý kiến và yêu cầu gì khác liên quan đến nhà đất này.
103. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, bị đơn ông
104. Trần Quốc H trình bày:
105. Ông  thống  nhất  với  lời  khai  của  nguyên  đơn  về  quan  hệ  nhân  thân  và  hàng
106. thừa kế và tài sản của cha mẹ ông là  ông Trần Văn Q1 (Trần Văn Q1) và bà Trần
107. Thị  M  để  lại.  Cha  mẹ  ông  mất  nhưng  không  để  lại  di  chúc.  Toàn  bộ  các  anh  em
108. trong gia đình đều thống nhất thỏa Thuận cho ông toàn quyền quản lý, sử dụng đối
109. với  diện  tích  đất  này,  việc  thỏa  thuận  tại  “Tờ  thỏa  thuận  phân  chia  di  sản”  ngày
110. 20/7/2009 đã được Ủy ban nhân dân xã A xác nhận, tức là quyền sử dụng đất đó là
111. tài sản của ông và ông có toàn quyền về tài sản này. Còn tài sản trên đất thì các anh
112. em trong gia đình  chưa phân chia cho ai. Khi ký tờ thỏa Thuận, tất cả các anh em
113. của ông đều tự nguyện, không nhầm lẫn, không bị ai lừa dối hay ép buộc, đe dọa gì,
114. cũng không phải là giả tạo để che giấu một giao dịch nào khác. Khi ký tờ thỏa thuận
115. trên  thì  các  anh  em  không  nói  với  ông  việc  không  được  chuyển  nhượng  quyền  sử
116. dụng đất, tại tờ thỏa thuận phân chia di sản cũng không có nội dung nào về việc ông
117. không được chuyển nhượng cho người khác.  Ông không hứa với các anh em trong
118. gia  đình  là  sẽ  không  chuyển  nhượng.  Do  đó,  ông  không  đồng  ý  với  yêu  cầu  của
119. nguyên đơn về chia đất, chỉ đồng ý chia tài sản trên đất, ông có nguyện vọng được
120. nhận  tài  sản  trên  đất  và  thanh  toán  giá  trị  lại  cho  mười  người  còn  lại.  Ngày
121. 02/4/2010,  ông kết  hôn với  chị  Châu  Ngọc  C, đến năm  2015 thì ly  hôn. Đến  ngày
122. 11/6/2016, ông kết hôn với chị Phạm Thị E.
123. Năm 2011, ông có thế chấp quyền sử dụng đất trên để vay tiền tại ngân hàng
124. HD  Bank, mục  đích vay  vốn kinh doanh, khi  ông  thế  chấp quyền sử dụng đất  ông
125. không nói với các anh em trong gia đình vì đây là đất của ông. Do không trả được nợ
126. nên ngân hàng đã kiện ông ra tòa, Tòa án đã xét xử bằng bản án và đã có hiệu lực
127. pháp luật, đã có quyết định thi hành án kê biên, xử lý tài sản nhưng chưa kê biên.
128. Phần đất trên hiện do ông Trần Văn T, bà Trần Thị Bích Th, bà Trần Thị Thúy
129. N, cháu Trần Văn R, cháu Trần Thị Th V và con của chị V là cháu Trần Hạo X và
130. ông đang quản lý, sử dụng. Sau này, ông sẽ lo chỗ ở cho các anh chị của ông là bà
131. Th, bà N, ông T là những người có tên trong hộ khẩu của ông nhưng ông không đề
132. nghị Tòa án ghi nhận trong vụ án này mà ông sẽ tự giải quyết riêng. Ông cũng không
133. hứa với bà Th như bà Th trình bày. Trong thời gian ở trên đất thì ông có sửa chữa
134. nhà  để  ở  nhưng  ông  không  yêu  cầu  gì.  Ông  không  yêu  cầu  giải  quyết  chi  phí  cho
135. việc bảo quản di sản hay yêu cầu nào khác.
136. Ông đã đăng ký cấp đổi  giấy chứng nhận  quyền sử dụng đất vào năm 2011,
137. đến  ngày  07/8/2015  mới  được  cấp  Giấy  chứng  nhận  quyền  sử  dụng  đất  số  BV
138. 102629. Hiện nay giấy này vẫn còn đang ở Ủy ban nhân dân xã A, ông chưa được
139. nhận, lý do vì sao thì ông không biết.
140. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
141. 23/01/2017 giữa ông và vợ ông là bà Phạm Thị E với anh H1 Thái Th1, chị Hồ Thị
142. Ngọc O, ông không có yêu cầu gì. Đất này là của ông nên ông có quyền ký hợp đồng
143. này. Ông không đồng ý đề nghị của bà Th về việc bán 5m chiều ngang đất, phần còn
144. lại để ở vì đất là của ông thì ông có quyền bán hết để trả nợ cho ngân hàng, nếu bán
145. 5m ngang thì không đủ trả nợ cho ngân hàng.
146. - Tại các bản tự khai, biên bản hòa giải  và trong quá trình  xét xử, người có
147. quyền lợi, nghĩa vụ liên quan là các ông bà Trần Thị Đan Ng, Trần Thị Lệ K, Trần
148. Thị Bích Th, Trần Thị Thúy N, Trần Văn Q, Trần Quang H1 trình bày:
149. Các ông bà thống nhất với lời trình bày và yêu cầu của nguyên đơn. Riêng đối
150. với tờ thỏa thuận phân chia di sản lập ngày 20/7/2009 tại xã A thì các ông, bà có biết
151. nội dung của tờ thỏa thuận đã có tại hồ sơ vụ án nhưng chỉ ký với mục đích để cho
152. ông H đứng tên trên sổ đỏ thôi. Các ông bà không còn lưu giữ tờ thỏa thuận này.
153. Trong  thời  gian  ở  trên  đất  thì  bà  Th,  bà  N,  ông  T  không  sửa  chữa  hay  xây
154. thêm công trình gì trên đất nên không có yêu cầu gì, không yêu cầu giải  quyết chi
155. phí  cho việc bảo quản di  sản.  Các ông  bà  chỉ  đề nghị  Tòa  án chia thừa  kế  nhà  đất
156. như nguyên đơn yêu cầu. Ngoài ra, không có ý kiến và yêu cầu gì khác. Đối với hợp
157. đồng đặt cọc mua bán đất giữa ông H và ông Th1 thì tự hai người này giải quyết, các
158. ông bà không yêu cầu gì.
159. Riêng bà Th có trình bày thêm: Ông H có hứa sẽ cắt cho bà 1/3 diện tích đất
160. trên để ở, bà không đồng ý cho ông H chuyển nhượng quyền sử dụng đất cho người
161. khác. Tại phiên tòa ngày 20/6/2018, bà đề nghị ông H bán 5m chiều ngang đất, phần
162. còn lại để ở.
163. Bà Th, bà N cho rằng trước khi ký hợp đồng đặt cọc bán đất thì ông H ép hai
164. bà ký và hai bà có ra điều kiện là ông H phải cắt một phần đất cho hai bà ở rồi mới
165. ký. Bà Th, bà N không có chứng cứ gì về vấn đề này.
166. - Người có quyền lợi, nghĩa vụ liên quan ông Trần Văn T và Trần Đình P, bà
167. Phạm Thị E do ông Trần Quốc H là đại diện theo ủy quyền trình bày:
168. Trước đây ông P có ý kiến là đồng ý với yêu cầu khởi kiện của nguyên đơn.
169. Nhưng  sau  đó  ông  P  đã  thay  đổi  ý  kiến  và  đã  ủy  quyền  cho  ông  đến  Tòa  án  giải
170. quyết tranh chấp. Ông T, ông P xác định diện tích đất tranh chấp đã được phân chia
171. cho ông. Ông T và ông P, bà E thống nhất với ý kiến của ông. Ngoài ra, không có ý
172. kiến nào khác, ông T không yêu cầu giải quyết chi phí cho việc bảo quản di sản hay
173. yêu cầu nào khác.
174. -  Người  có  quyền  lợi,  nghĩa  vụ  liên  quan  bà  Nguyễn  Thị  Th  P  do  ông  Trần
175. Văn T là đại diện theo ủy quyền trình bày:
176. Bà P thống nhất lời trình bày của ông T.
177. - Tại các bản tự khai, người có quyền lợi, nghĩa vụ liên quan anh Trần Văn R,
178. chị Trần Thị Th V trình bày:
179. Anh, chị là con của ông Trần Văn T, anh chị không có công sức đóng góp gì
180. trên diện tích đất tranh chấp, không có ý kiến gì và hoàn toàn nhường quyền lại cho
181. ông T. Anh chị xin vắng mặt tất cả các buổi triệu tập trong quá trình giải quyết vụ án
182. cho đến khi vụ án kết thúc và có bản án có hiệu lực pháp luật.
183. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
184. quyền lợi, nghĩa vụ liên quan Ngân hàng thương mại cổ phần Y do anh Nguyễn Hữu
185. S là đại diện theo ủy quyền trình bày:
186. là  ngân  hàng)  300.000.000  đồng
187. Ngày 23/6/2011, ông H và bà Châu Ngọc C có vay tiền của ngân hàng Y (gọi tắt số
188. 00151/HĐTDNH/HDB ngày 23/6/2011. Tài sản đảm bảo là  quyền sử dụng đất đối
189. với thửa đất số 101, tờ bản đồ số 01 xã A, diện tích 488m2 (Nay là diện tích 432,1m2
190. Thộc  thửa  số  51,  tờ  bản  đồ  số  27  xã  A)  theo  Hợp  đồng  thế  chấp  tài  sản  số
191. 00151/HĐTC/HDB ngày 23/6/2011, hợp đồng đã được công chứng, chứng thực tại
192. UBND  xã  A,  huyện  L,  tỉnh  Đồng  Nai,  đăng  ký  giao  dịch  bảo  đảm  tại  Phòng  tài
193. nguyên và môi trường huyện L, tỉnh Đồng Nai vào ngày 23/6/2011.
194. theo  Hợp  đồng
195. tín  dụng
196. Trong quá trình thực hiện hợp đồng, ông H và bà C đã vi phạm nghĩa vụ trả
197. nợ nên Ngân hàng đã khởi kiện ông H và bà C ra Tòa án nhân dân huyện L. Ngày
198. 16/7/2012,  Tòa  án  đã  xét  xử  bằng  bản  án  số  04/2012/KDTM-ST  ngày  16/7/2012,
199. buộc ông H và bà C phải thanh toán nợ cho ngân hàng. Tài sản thế chấp là quyền sử
200. dụng đất đối với thửa đất số 101, tờ bản đồ số 01, tổng diện tích 488m2 được đảm
201. bảo thi hành án.
202. Ngày  27/11/2013,  chi  cục  thi  hành  án  dân  sự  huyện  L  đã  ra  quyết  định  kê
203. biên, xử lý tài sản số 50/QĐ-CCTHA ngày 14/4/2014. Hiện nay cơ quan thi hành án
204. vẫn đang tiến hành thi hành bản án số 04 nêu trên của Tòa án nhưng chưa kê biên,
205. xử lý tài sản thế chấp do đang có tranh chấp.
206. Nay Ngân hàng đề nghị Tòa án xem xét, giải quyết vụ án theo đúng quy định
207. pháp luật để Chi cục thi hành án dân sự huyện L, tỉnh Đồng Nai tiếp tục thi hành bản
208. án số 04 nêu trên để bảo vệ quyền, lợi ích hợp pháp cho Ngân hàng.
209. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
210. quyền lợi, nghĩa vụ liên quan anh H1 Thái Th1 trình bày:
211. Yêu cầu Tòa án giải quyết vụ án theo pháp luật, anh và vợ anh là chị O không
212. có ý kiến gì đối với yêu cầu của nguyên đơn. Đối với Hợp đồng đặt cọc và chuyển
213. nhượng quyền sử dụng đất ngày 23/01/2017 giữa vợ chồng anh và vợ chồng anh H,
214. anh chị sẽ đợi Tòa án giải  quyết xong vụ án tranh chấp thừa kế này rồi sẽ tiếp tục
215. giao  dịch  mua  bán  đất.  Hợp  đồng  đặt  cọc  này  được  ký  tại  nhà  đất  mà  đang  tranh
216. chấp trong vụ án này và có những người anh em của ông H đã ký tên làm chứng vào
217. hợp đồng, khi ký thì những người này vui vẻ, không bị ai ép buộc gì.
218. - Ý kiến phát biểu của đại diện Viện kiểm sát nhân dân huyện Long Thành:
219. Tại phiên tòa, đại diện Viện kiểm sát nhân dân huyện Long Thành phát biểu ý
220. kiến  về  việc  tuân  theo  pháp  luật  của  Thẩm  phán,  Hội  đồng  xét  xử  được  thực  hiện
221. đúng theo quy định của Bộ luật tố tụng dân sự từ khi Tòa án thụ lý vụ án đến khi Hội
222. đồng  xét xử  vào  phòng nghị  án. Việc  chấp  hành  pháp  luật  của  các  đương  sự  được
223. thực hiện theo quy định của Bộ luật Tố tụng dân sự.
224. Về việc giải quyết vụ án: Về nguồn gốc tài sản đang tranh chấp gồm có quyền
225. sử dụng diện tích đất 432,1m2 thuộc thửa số 51, tờ bản đồ số 11, xã A và tài sản gắn
226. liền với đất có nguồn gốc là do ông Q1, bà M tạo lập ra. Vào năm 2007 ông Q1 chết,
227. năm 2008 bà M chết và không để lại di chúc, các bên đương sự thống nhất thừa nhận
228. sự việc này. Ngày 20/7/2009, mười một anh em trong gia đình ông Đ, ông T, ông H
229. lập tờ thỏa thuận phân chia di sản thừa kế có xác nhận của Ủy ban nhân dân xã  A.
230. Tại tờ thỏa thuận này mười một anh em trong gia đình đã phân chia diện tích đất nêu
231. trên cho ông H toàn quyền quản lý, sử dụng trên cơ sở tự nguyện, không bị ép buộc, đe dọa, không trái pháp luật và đạo đức xã hội. Việc ông Đ, ông T cho rằng các anh chị em trong gia đình chỉ thống nhất giao diện tích đất nêu trên cho ông H thay mặt các  anh  chị  em  đi đăng  ký kê  khai  cấp  đổi giấy  chứng nhận  quyền  sử dụng đất và đứng tên giấy chứng nhận, chỉ giao cho ông H nhà đất để ở và không được chuyển nhượng  cho  người  khác,  chứ  không  cho  ông  H  toàn  bộ  tài  sản  do  cha  …
232. Riêng đối với tài sản là các căn nhà và công trình trên đất, các bên  đương sự đều thừa nhận là tài sản do cha mẹ chết để lại, tại thời điểm lập tờ thỏa thuận phân chia  di sản thừa  kế  các  bên đương sự  chưa  thỏa thuận phân chia, chưa  giao  quyền quản lý, sử dụng và định đoạt các tài sản này. Cụ thể, hiện tại trên đất có bà N, ông T, ông H, bà Th, các con của ông T là R, V đang quản lý, sử dụng các căn nhà do cha mẹ của ông Đ, ông T, ông H đã xây dựng trước đó. Do đó, tài sản này là được …
233. xem xét quyết định.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
2. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
3. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
4. [BLDS 2015] Điều 623. Thời hiệu thừa kế. 1. Thời hiệu để người thừa kế yêu cầu chia di sản là 30 năm đối với bất động sản, 10 năm đối với động sản, kể từ thời điểm mở thừa kế. Hết thời hạn này thì di sản thuộc về người thừa kế đang quản lý di sản đó. Trường hợp không có người thừa kế đang quản lý di sản thì di sản được giải quyết như sau: a) Di sản thuộc quyền sở hữu của người đang chiếm hữu theo quy định tại Điều 236 của Bộ luật này; b) Di sản thuộc về Nhà nước, nếu không có người chiếm hữu quy định tại điểm a khoản này. 2. Thời hiệu để người thừa kế yêu cầu xác nhận quyền thừa kế của mình hoặc bác bỏ quyền thừa kế của người khác là 10 năm, kể từ thời điểm mở thừa kế. 3. Thời hiệu yêu cầu người thừa kế thực hiện
5. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá yêu cầu của nguyên đơn có được chấp nhận toàn bộ hay một phần, chúng ta cần phân tích từng yếu tố trong vụ án:

1. Theo yêu cầu của nguyên đơn, họ yêu cầu chia di sản thừa kế gồm diện tích đất 432,1m2 và tài sản gắn liền với đất trị giá 1.692.700.000 đồng.

2. Theo lời khai của bị đơn và các người có quyền lợi, nghĩa vụ liên quan, họ đồng ý chia tài sản trên đất, nhưng không đồng ý chia đất. Thay vào đó, họ đề nghị chia tài sản trên đất và nhận tài sản trên đất.

3. Theo Điều 660 BLDS 2015, khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản. Tuy nhiên, trong vụ án này không có trường hợp này.

4. Theo Điều 659 BLDS 2015, việc phân chia di sản theo di chúc được thực hiện theo ý chí của người để lại di chúc. Trong vụ án này, không có di chúc xác định phân chia di sản.

5. Theo Điều 662 BLDS 2015, nếu đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật. Trong vụ án này, không có trường hợp này.

6. Theo Điều 623 BLDS 2015, thời hiệu yêu cầu chia di sản là 30 năm đối với bất động sản. Thời hiệu này đã hết, di sản thuộc về người đang quản lý di sản.

Như vậy, mặc dù nguyên đơn yêu cầu chia di sản bằng hiện vật, nhưng các đương sự không đồng ý chia đất. Họ đề nghị chia tài sản trên đất và nhận tài sản trên đất. Điều này phù hợp với quy định của pháp luật.

Yêu cầu của nguyên đơn được chấp nhận (tất cả).
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. - Người có quyền lợi, nghĩa vụ liên quan:
2. Ông Trần Văn Q, sinh năm 1966.
3. Địa chỉ: Số 30, tổ 10, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
4. Ông Trần Quang H1, sinh năm 1972.
5. Địa chỉ:  tổ 12, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
6. Bà Trần Thị Thúy N, sinh năm 1961.
7. Bà Trần Thị Bích Th, sinh năm 1963.
8. Ông Trần Văn T, sinh năm 1959.
9. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, Đồng Nai.
10. Ông  T  ủy  quyền  cho  ông  Trần  Quốc  H  theo  văn  bản  ủy  quyền  ngày
11. 07/3/2017.
12. 6/ Ông Trần Đình P, sinh năm 1970.
13. Địa chỉ: xã C, huyện L, tỉnh Đồng Nai.
14. Ông P ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 08/3/2017.
15. 7/ Bà Trần Thị Đan Ng, sinh năm 1953.
16. Địa chỉ: Số 45 N, phường 19, quận M, TP. Hồ Chí Minh.
17. 8/ Bà Trần Thị Lệ K, sinh năm 1974.
18. Địa chỉ: Số 19B, tổ 12, khu S, thị trấn L, huyện L, Đồng Nai.
19. 9/ Bà Nguyễn Thị Th P, sinh năm 1971.
20. Địa chỉ: tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
21. Bà P ủy quyền cho ông Trần Văn T theo văn bản ủy quyền ngày 16/10/2017.
22. 10/ Chị Trần Thị Th V, sinh năm 1992.
23. 11/  Cháu  Trần  Hạo  X,  sinh  ngày  27/10/2013.  Do  chị  V  đại  diện  theo  pháp
24. 12/ Anh Trần Văn R, sinh năm 1994.
25. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
26. 13/ Anh Hoàng Thái Th1, sinh năm 1989.
27. 14/ Chị Hồ Thị Ngọc O, sinh năm 1988.
28. Địa chỉ: Ấp 2, xã Z, huyện L, tỉnh Đồng Nai.
29. Chị O ủy quyền cho anh Hoàng Thái Th1.
30. 15/ Ngân hàng thương mại cổ phần Y.
31. Địa chỉ: 25 bis A, phường B, quận C, TP. Hồ Chí Minh.
32. Người  đại  diện  theo  pháp  luật:  Ông  Nguyễn  Hữu  D  –  chức  vụ:  Tổng  giám
33. luật.
34. đốc.
35. Người đại diện theo ủy quyền: Anh Nguyễn Hữu S – Nhân viên ngân hàng.
36. 16/ Bà Phạm Thị E, sinh năm 1979.
37. Địa chỉ: Số 390 khu 1, thị trấn L, huyện L, tỉnh Đồng Nai.
38. Bà E ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 17/11/2017.
39. (Ông Đ, ông T, ông H, ông Q, ông H1, bà N, bà Th, bà Ng, bà K, anh Th1,
40. anh S có mặt, anh R, chị V đề nghị vắng mặt).
41. NỘI DUNG VỤ ÁN:
42. -  Tại  đơn  khởi  kiện  ngày  10  tháng  02  năm  2017  và  trong  quá  trình  xét  xử,
43. nguyên đơn ông Trần Văn Đ, ông Trần Văn T trình bày:
44. Cha mẹ của hai ông là Trần Văn Q1 (Trần Văn Q1), sinh năm 1923, mất năm
45. 2007; bà Trần Thị M, sinh năm 1931, mất năm 2008. Cha mẹ của ông Q1 và bà M
46. đã mất từ lâu. Ông Q1 và bà M sinh được 15 người con, chết 04 người khi còn trẻ và
47. chưa lập gia đình, hiện giờ còn 11 người, tên là:
48. Ông Trần Văn Đ, sinh năm 1951.
49. Bà Trần Thị Đan Ng, sinh năm 1953.
50. Ông Trần Văn T, sinh năm 1959.
51. Bà Trần Thị Thúy N, sinh năm 1961.
52. Bà Trần Thị Bích Th, sinh năm 1963.
53. Ông Trần Văn T, sinh năm 1964.
54. Ông Trần Văn Q, sinh năm 1966.
55. Ông Trần Đình P, sinh năm 1970.
56. Ông Trần Quang H1, sinh năm 1972.
57. Bà Trần Thị Lệ K, sinh năm 1974.
58. Ông Trần Quốc H, sinh năm 1976.
59. Ông Q1, bà M không còn người con chung hay con riêng, con nuôi nào khác.
60. Ông Q1 và bà M để lại tài sản chung là diện tích đất 488m2 thửa đất số 101, tờ
61. bản đồ số 1 xã  A, huyện L, tỉnh Đồng Nai và tài sản gắn liền với đất. Nay là diện
62. tích đất 432,1m2 Thộc thửa 51, tờ bản đồ số 11 xã A theo bản đồ hiện trạng thửa đất
63. số 8603/2017 ngày 30/6/2017 của Văn phòng đăng ký đất đai tỉnh  Đồng Nai – chi
64. nhánh L.
65. Khi ông Q1, bà M mất thì không để lại di chúc. Tất cả anh em trong gia đình
66. có ký vào tờ thỏa thuận phân chia di sản ngày 20/7/2009 tại UBND xã A để cho ông
67. H thay mặt các anh em đứng tên quản lý, sử dụng đất nhưng không biết nội dung tờ
68. thỏa thuận là gì, vì khi ký ông H chỉ đưa cho các anh em ký vào tờ giấy trắng chứ
69. không có nội dung gì trên đó. Tuy nhiên hai ông không photo tờ giấy trắng có chữ
70. ký đó lại nên không có tài liệu để cung cấp cho Tòa án. Hai ông có nói với ông H là
71. chỉ được quản lý, sử dụng diện tích đất trên để ở và không được chuyển nhượng cho
72. người khác. Ông H cũng hứa với các anh em là chỉ ở và sẽ không chuyển nhượng.
73. Tại phiên tòa ngày 26/4/2018, hai ông thừa nhận là có biết nội dung tại tờ thỏa
74. thuận như có tại hồ sơ vụ án nhưng chỉ ký với mục đích là cho ông H đứng tên trên
75. giấy chứng nhận quyền sử dụng đất mà thôi.
76. Khi ký, tất cả các anh em đều tự nguyện, không nhầm lẫn, không bị ai lừa dối
77. hay ép buộc, đe dọa gì. Tờ thỏa thuận phân chia di sản ngày 20/7/2009 cũng không
78. phải là giả tạo để che giấu một giao dịch nào khác.
79. Hiện  nay  trên  phần  đất  đó  có  bà  Trần  Thị  Bích  Th  (độc  thân),  bà  Trần  Thị
80. Thúy N (độc thân), ông Trần Văn T (độc thân) và ông Trần Quốc H, các con của ông
81. T là Trần Văn R (độc thân), Trần Thị Th V (độc thân), con của chị V là cháu Trần
82. Hạo X đang sinh sống. Trước đây vợ cV ông T có sống trên đất này nhưng  vợ cV
83. ông đã chuyển chỗ ở sang nhà kế bên đất đang tranh chấp, còn phòng ở do ông sử
84. dụng trước đây thì hiện nay con trai là Trần Văn R đang sử dụng, còn con gái tên V
85. và cháu X thì ở chung phòng với bà Th. Trong thời gian ở trên đất thì ông T có sửa
86. chữa  nhà  nhưng  ông  không  yêu  cầu  gì,  không  yêu  cầu  giải  quyết  chi  phí  cho  việc
87. bảo quản di sản hay yêu cầu nào khác. Việc ông H thế chấp phần đất trên để vay vốn
88. ngân hàng thì hai ông không hề biết.
89. Nay ông Đ, ông T yêu cầu Tòa án phân chia di sản thừa kế của ông Q1 và bà
90. M để lại là diện tích đất 432,1m2 thửa số 51, tờ bản đồ số 11 xã  A, huyện L và tài
91. sản  gắn  liền  với  đất,  trị  giá  1.692.700.000  đồng  theo  Chứng  thư  thẩm  định  giá  số
92. 2103/TĐG-CT ngày 31/8/2017 của Công ty cổ phần thẩm định giá Đồng Nai thành
93. 11 phần bằng nhau theo giá trị. Yêu cầu để ông T nhận di sản bằng hiện vật là nhà
94. đất và thanh toán giá trị cho 10 người còn lại, mỗi người được hưởng 1/10 giá trị của
95. tài sản, tương đương với số tiền là 169.270.000 đồng. Ông Đ, ông T không yêu cầu
96. thẩm định giá lại tài sản tranh chấp, đề nghị Tòa án áp dụng chứng thư thẩm định giá
97. có tại hồ sơ vụ án để giải quyết.
98. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
99. 23/01/2017 giữa ông Trần Quốc H, bà Phạm Thị E với ông H1 Thái Th1, chị Hồ Thị
100. Ngọc O thì ông Đ, ông T không đồng ý. Tuy nhiên, hai ông không có yêu cầu gì đối
101. với hợp đồng này, việc này tự ông H và ông Th1 giải quyết. Ngoài ra, ông Đ, ông T
102. không có ý kiến và yêu cầu gì khác liên quan đến nhà đất này.
103. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, bị đơn ông
104. Trần Quốc H trình bày:
105. Ông  thống  nhất  với  lời  khai  của  nguyên  đơn  về  quan  hệ  nhân  thân  và  hàng
106. thừa kế và tài sản của cha mẹ ông là  ông Trần Văn Q1 (Trần Văn Q1) và bà Trần
107. Thị  M  để  lại.  Cha  mẹ  ông  mất  nhưng  không  để  lại  di  chúc.  Toàn  bộ  các  anh  em
108. trong gia đình đều thống nhất thỏa Thuận cho ông toàn quyền quản lý, sử dụng đối
109. với  diện  tích  đất  này,  việc  thỏa  thuận  tại  “Tờ  thỏa  thuận  phân  chia  di  sản”  ngày
110. 20/7/2009 đã được Ủy ban nhân dân xã A xác nhận, tức là quyền sử dụng đất đó là
111. tài sản của ông và ông có toàn quyền về tài sản này. Còn tài sản trên đất thì các anh
112. em trong gia đình  chưa phân chia cho ai. Khi ký tờ thỏa Thuận, tất cả các anh em
113. của ông đều tự nguyện, không nhầm lẫn, không bị ai lừa dối hay ép buộc, đe dọa gì,
114. cũng không phải là giả tạo để che giấu một giao dịch nào khác. Khi ký tờ thỏa thuận
115. trên  thì  các  anh  em  không  nói  với  ông  việc  không  được  chuyển  nhượng  quyền  sử
116. dụng đất, tại tờ thỏa thuận phân chia di sản cũng không có nội dung nào về việc ông
117. không được chuyển nhượng cho người khác.  Ông không hứa với các anh em trong
118. gia  đình  là  sẽ  không  chuyển  nhượng.  Do  đó,  ông  không  đồng  ý  với  yêu  cầu  của
119. nguyên đơn về chia đất, chỉ đồng ý chia tài sản trên đất, ông có nguyện vọng được
120. nhận  tài  sản  trên  đất  và  thanh  toán  giá  trị  lại  cho  mười  người  còn  lại.  Ngày
121. 02/4/2010,  ông kết  hôn với  chị  Châu  Ngọc  C, đến năm  2015 thì ly  hôn. Đến  ngày
122. 11/6/2016, ông kết hôn với chị Phạm Thị E.
123. Năm 2011, ông có thế chấp quyền sử dụng đất trên để vay tiền tại ngân hàng
124. HD  Bank, mục  đích vay  vốn kinh doanh, khi  ông  thế  chấp quyền sử dụng đất  ông
125. không nói với các anh em trong gia đình vì đây là đất của ông. Do không trả được nợ
126. nên ngân hàng đã kiện ông ra tòa, Tòa án đã xét xử bằng bản án và đã có hiệu lực
127. pháp luật, đã có quyết định thi hành án kê biên, xử lý tài sản nhưng chưa kê biên.
128. Phần đất trên hiện do ông Trần Văn T, bà Trần Thị Bích Th, bà Trần Thị Thúy
129. N, cháu Trần Văn R, cháu Trần Thị Th V và con của chị V là cháu Trần Hạo X và
130. ông đang quản lý, sử dụng. Sau này, ông sẽ lo chỗ ở cho các anh chị của ông là bà
131. Th, bà N, ông T là những người có tên trong hộ khẩu của ông nhưng ông không đề
132. nghị Tòa án ghi nhận trong vụ án này mà ông sẽ tự giải quyết riêng. Ông cũng không
133. hứa với bà Th như bà Th trình bày. Trong thời gian ở trên đất thì ông có sửa chữa
134. nhà  để  ở  nhưng  ông  không  yêu  cầu  gì.  Ông  không  yêu  cầu  giải  quyết  chi  phí  cho
135. việc bảo quản di sản hay yêu cầu nào khác.
136. Ông đã đăng ký cấp đổi  giấy chứng nhận  quyền sử dụng đất vào năm 2011,
137. đến  ngày  07/8/2015  mới  được  cấp  Giấy  chứng  nhận  quyền  sử  dụng  đất  số  BV
138. 102629. Hiện nay giấy này vẫn còn đang ở Ủy ban nhân dân xã A, ông chưa được
139. nhận, lý do vì sao thì ông không biết.
140. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
141. 23/01/2017 giữa ông và vợ ông là bà Phạm Thị E với anh H1 Thái Th1, chị Hồ Thị
142. Ngọc O, ông không có yêu cầu gì. Đất này là của ông nên ông có quyền ký hợp đồng
143. này. Ông không đồng ý đề nghị của bà Th về việc bán 5m chiều ngang đất, phần còn
144. lại để ở vì đất là của ông thì ông có quyền bán hết để trả nợ cho ngân hàng, nếu bán
145. 5m ngang thì không đủ trả nợ cho ngân hàng.
146. - Tại các bản tự khai, biên bản hòa giải  và trong quá trình  xét xử, người có
147. quyền lợi, nghĩa vụ liên quan là các ông bà Trần Thị Đan Ng, Trần Thị Lệ K, Trần
148. Thị Bích Th, Trần Thị Thúy N, Trần Văn Q, Trần Quang H1 trình bày:
149. Các ông bà thống nhất với lời trình bày và yêu cầu của nguyên đơn. Riêng đối
150. với tờ thỏa thuận phân chia di sản lập ngày 20/7/2009 tại xã A thì các ông, bà có biết
151. nội dung của tờ thỏa thuận đã có tại hồ sơ vụ án nhưng chỉ ký với mục đích để cho
152. ông H đứng tên trên sổ đỏ thôi. Các ông bà không còn lưu giữ tờ thỏa thuận này.
153. Trong  thời  gian  ở  trên  đất  thì  bà  Th,  bà  N,  ông  T  không  sửa  chữa  hay  xây
154. thêm công trình gì trên đất nên không có yêu cầu gì, không yêu cầu giải  quyết chi
155. phí  cho việc bảo quản di  sản.  Các ông  bà  chỉ  đề nghị  Tòa  án chia thừa  kế  nhà  đất
156. như nguyên đơn yêu cầu. Ngoài ra, không có ý kiến và yêu cầu gì khác. Đối với hợp
157. đồng đặt cọc mua bán đất giữa ông H và ông Th1 thì tự hai người này giải quyết, các
158. ông bà không yêu cầu gì.
159. Riêng bà Th có trình bày thêm: Ông H có hứa sẽ cắt cho bà 1/3 diện tích đất
160. trên để ở, bà không đồng ý cho ông H chuyển nhượng quyền sử dụng đất cho người
161. khác. Tại phiên tòa ngày 20/6/2018, bà đề nghị ông H bán 5m chiều ngang đất, phần
162. còn lại để ở.
163. Bà Th, bà N cho rằng trước khi ký hợp đồng đặt cọc bán đất thì ông H ép hai
164. bà ký và hai bà có ra điều kiện là ông H phải cắt một phần đất cho hai bà ở rồi mới
165. ký. Bà Th, bà N không có chứng cứ gì về vấn đề này.
166. - Người có quyền lợi, nghĩa vụ liên quan ông Trần Văn T và Trần Đình P, bà
167. Phạm Thị E do ông Trần Quốc H là đại diện theo ủy quyền trình bày:
168. Trước đây ông P có ý kiến là đồng ý với yêu cầu khởi kiện của nguyên đơn.
169. Nhưng  sau  đó  ông  P  đã  thay  đổi  ý  kiến  và  đã  ủy  quyền  cho  ông  đến  Tòa  án  giải
170. quyết tranh chấp. Ông T, ông P xác định diện tích đất tranh chấp đã được phân chia
171. cho ông. Ông T và ông P, bà E thống nhất với ý kiến của ông. Ngoài ra, không có ý
172. kiến nào khác, ông T không yêu cầu giải quyết chi phí cho việc bảo quản di sản hay
173. yêu cầu nào khác.
174. -  Người  có  quyền  lợi,  nghĩa  vụ  liên  quan  bà  Nguyễn  Thị  Th  P  do  ông  Trần
175. Văn T là đại diện theo ủy quyền trình bày:
176. Bà P thống nhất lời trình bày của ông T.
177. - Tại các bản tự khai, người có quyền lợi, nghĩa vụ liên quan anh Trần Văn R,
178. chị Trần Thị Th V trình bày:
179. Anh, chị là con của ông Trần Văn T, anh chị không có công sức đóng góp gì
180. trên diện tích đất tranh chấp, không có ý kiến gì và hoàn toàn nhường quyền lại cho
181. ông T. Anh chị xin vắng mặt tất cả các buổi triệu tập trong quá trình giải quyết vụ án
182. cho đến khi vụ án kết thúc và có bản án có hiệu lực pháp luật.
183. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
184. quyền lợi, nghĩa vụ liên quan Ngân hàng thương mại cổ phần Y do anh Nguyễn Hữu
185. S là đại diện theo ủy quyền trình bày:
186. là  ngân  hàng)  300.000.000  đồng
187. Ngày 23/6/2011, ông H và bà Châu Ngọc C có vay tiền của ngân hàng Y (gọi tắt số
188. 00151/HĐTDNH/HDB ngày 23/6/2011. Tài sản đảm bảo là  quyền sử dụng đất đối
189. với thửa đất số 101, tờ bản đồ số 01 xã A, diện tích 488m2 (Nay là diện tích 432,1m2
190. Thộc  thửa  số  51,  tờ  bản  đồ  số  27  xã  A)  theo  Hợp  đồng  thế  chấp  tài  sản  số
191. 00151/HĐTC/HDB ngày 23/6/2011, hợp đồng đã được công chứng, chứng thực tại
192. UBND  xã  A,  huyện  L,  tỉnh  Đồng  Nai,  đăng  ký  giao  dịch  bảo  đảm  tại  Phòng  tài
193. nguyên và môi trường huyện L, tỉnh Đồng Nai vào ngày 23/6/2011.
194. theo  Hợp  đồng
195. tín  dụng
196. Trong quá trình thực hiện hợp đồng, ông H và bà C đã vi phạm nghĩa vụ trả
197. nợ nên Ngân hàng đã khởi kiện ông H và bà C ra Tòa án nhân dân huyện L. Ngày
198. 16/7/2012,  Tòa  án  đã  xét  xử  bằng  bản  án  số  04/2012/KDTM-ST  ngày  16/7/2012,
199. buộc ông H và bà C phải thanh toán nợ cho ngân hàng. Tài sản thế chấp là quyền sử
200. dụng đất đối với thửa đất số 101, tờ bản đồ số 01, tổng diện tích 488m2 được đảm
201. bảo thi hành án.
202. Ngày  27/11/2013,  chi  cục  thi  hành  án  dân  sự  huyện  L  đã  ra  quyết  định  kê
203. biên, xử lý tài sản số 50/QĐ-CCTHA ngày 14/4/2014. Hiện nay cơ quan thi hành án
204. vẫn đang tiến hành thi hành bản án số 04 nêu trên của Tòa án nhưng chưa kê biên,
205. xử lý tài sản thế chấp do đang có tranh chấp.
206. Nay Ngân hàng đề nghị Tòa án xem xét, giải quyết vụ án theo đúng quy định
207. pháp luật để Chi cục thi hành án dân sự huyện L, tỉnh Đồng Nai tiếp tục thi hành bản
208. án số 04 nêu trên để bảo vệ quyền, lợi ích hợp pháp cho Ngân hàng.
209. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
210. quyền lợi, nghĩa vụ liên quan anh H1 Thái Th1 trình bày:
211. Yêu cầu Tòa án giải quyết vụ án theo pháp luật, anh và vợ anh là chị O không
212. có ý kiến gì đối với yêu cầu của nguyên đơn. Đối với Hợp đồng đặt cọc và chuyển
213. nhượng quyền sử dụng đất ngày 23/01/2017 giữa vợ chồng anh và vợ chồng anh H,
214. anh chị sẽ đợi Tòa án giải  quyết xong vụ án tranh chấp thừa kế này rồi sẽ tiếp tục
215. giao  dịch  mua  bán  đất.  Hợp  đồng  đặt  cọc  này  được  ký  tại  nhà  đất  mà  đang  tranh
216. chấp trong vụ án này và có những người anh em của ông H đã ký tên làm chứng vào
217. hợp đồng, khi ký thì những người này vui vẻ, không bị ai ép buộc gì.
218. - Ý kiến phát biểu của đại diện Viện kiểm sát nhân dân huyện Long Thành:
219. Tại phiên tòa, đại diện Viện kiểm sát nhân dân huyện Long Thành phát biểu ý
220. kiến  về  việc  tuân  theo  pháp  luật  của  Thẩm  phán,  Hội  đồng  xét  xử  được  thực  hiện
221. đúng theo quy định của Bộ luật tố tụng dân sự từ khi Tòa án thụ lý vụ án đến khi Hội
222. đồng  xét xử  vào  phòng nghị  án. Việc  chấp  hành  pháp  luật  của  các  đương  sự  được
223. thực hiện theo quy định của Bộ luật Tố tụng dân sự.
224. Về việc giải quyết vụ án: Về nguồn gốc tài sản đang tranh chấp gồm có quyền
225. sử dụng diện tích đất 432,1m2 thuộc thửa số 51, tờ bản đồ số 11, xã A và tài sản gắn
226. liền với đất có nguồn gốc là do ông Q1, bà M tạo lập ra. Vào năm 2007 ông Q1 chết,
227. năm 2008 bà M chết và không để lại di chúc, các bên đương sự thống nhất thừa nhận
228. sự việc này. Ngày 20/7/2009, mười một anh em trong gia đình ông Đ, ông T, ông H
229. lập tờ thỏa thuận phân chia di sản thừa kế có xác nhận của Ủy ban nhân dân xã  A.
230. Tại tờ thỏa thuận này mười một anh em trong gia đình đã phân chia diện tích đất nêu
231. trên cho ông H toàn quyền quản lý, sử dụng trên cơ sở tự nguyện, không bị ép buộc, đe dọa, không trái pháp luật và đạo đức xã hội. Việc ông Đ, ông T cho rằng các anh chị em trong gia đình chỉ thống nhất giao diện tích đất nêu trên cho ông H thay mặt các  anh  chị  em  đi đăng  ký kê  khai  cấp  đổi giấy  chứng nhận  quyền  sử dụng đất và đứng tên giấy chứng nhận, chỉ giao cho ông H nhà đất để ở và không được chuyển nhượng  cho  người  khác,  chứ  không  cho  ông  H  toàn  bộ  tài  sản  do  cha  …
232. Riêng đối với tài sản là các căn nhà và công trình trên đất, các bên  đương sự đều thừa nhận là tài sản do cha mẹ chết để lại, tại thời điểm lập tờ thỏa thuận phân chia  di sản thừa  kế  các  bên đương sự  chưa  thỏa thuận phân chia, chưa  giao  quyền quản lý, sử dụng và định đoạt các tài sản này. Cụ thể, hiện tại trên đất có bà N, ông T, ông H, bà Th, các con của ông T là R, V đang quản lý, sử dụng các căn nhà do cha mẹ của ông Đ, ông T, ông H đã xây dựng trước đó. Do đó, tài sản này là được …
233. xem xét quyết định.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
2. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
3. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
4. [BLDS 2015] Điều 623. Thời hiệu thừa kế. 1. Thời hiệu để người thừa kế yêu cầu chia di sản là 30 năm đối với bất động sản, 10 năm đối với động sản, kể từ thời điểm mở thừa kế. Hết thời hạn này thì di sản thuộc về người thừa kế đang quản lý di sản đó. Trường hợp không có người thừa kế đang quản lý di sản thì di sản được giải quyết như sau: a) Di sản thuộc quyền sở hữu của người đang chiếm hữu theo quy định tại Điều 236 của Bộ luật này; b) Di sản thuộc về Nhà nước, nếu không có người chiếm hữu quy định tại điểm a khoản này. 2. Thời hiệu để người thừa kế yêu cầu xác nhận quyền thừa kế của mình hoặc bác bỏ quyền thừa kế của người khác là 10 năm, kể từ thời điểm mở thừa kế. 3. Thời hiệu yêu cầu người thừa kế thực hiện
5. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng yếu tố trong vụ án theo các quy định của Bộ luật Dân sự 2015. Dựa trên thông tin cung cấp, tôi sẽ phân tích từng bước:

1. **Quan hệ thừa kế và tài sản thừa kế**:
   - Theo hồ sơ, ông Trần Văn Q1 và bà Trần Thị M đã mất, không để lại di chúc. Họ đã thống nhất phân chia di sản bằng tờ thỏa thuận ngày 20/7/2009, được UBND xã A xác nhận.
   - Theo thỏa thuận này, ông H được quyền quản lý, sử dụng diện tích đất 432,1m2 và tài sản gắn liền với đất.

2. **Thời hiệu thừa kế**:
   - Theo Điều 623 BLDS 2015, thời hiệu yêu cầu chia di sản đối với bất động sản là 30 năm kể từ thời điểm mở thừa kế. Vụ án này mở thừa kế từ năm 2007, nên thời hiệu đã hết vào năm 2037.
   - Vì vậy, yêu cầu chia di sản của ông Đ, ông T vượt quá thời hiệu, theo quy định của pháp luật.

3. **Phân chia di sản theo thỏa thuận**:
   - Theo Điều 659 BLDS 2015, nếu có thỏa thuận phân chia di sản, các bên phải thực hiện theo thỏa thuận đó. Trong trường hợp này, thỏa thuận đã được xác nhận bởi UBND xã A.
   - Theo thỏa thuận, ông H được quyền quản lý, sử dụng diện tích đất 432,1m2 và tài sản gắn liền với đất.

4. **Thời hiệu xác nhận quyền thừa kế**:
   - Theo Điều 623 BLDS 2015, thời hiệu để yêu cầu xác nhận quyền thừa kế là 10 năm kể từ thời điểm mở thừa kế. Vụ án này mở thừa kế từ năm 2007, nên thời hiệu đã hết vào năm 2017.
   - Vì vậy, yêu cầu xác nhận quyền thừa kế của ông Đ, ông T vượt quá thời hiệu, theo quy định của pháp luật.

5. **Thời hiệu bác bỏ quyền thừa kế**:
   - Theo Điều 623 BLDS 2015, thời hiệu để yêu cầu bác bỏ quyền thừa kế là 10 năm kể từ thời điểm mở thừa kế. Vụ án này mở thừa kế từ năm 2007, nên thời hiệu đã hết vào năm 2017.
   - Vì vậy, yêu cầu bác bỏ quyền thừa kế của ông Đ, ông T vượt quá thời hiệu, theo
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge
```

## A.3#1 — rule_based (defendant)

**Prompt**
```
Considering the following facts:
1. - Người có quyền lợi, nghĩa vụ liên quan:
2. Ông Trần Văn Q, sinh năm 1966.
3. Địa chỉ: Số 30, tổ 10, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
4. Ông Trần Quang H1, sinh năm 1972.
5. Địa chỉ:  tổ 12, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
6. Bà Trần Thị Thúy N, sinh năm 1961.
7. Bà Trần Thị Bích Th, sinh năm 1963.
8. Ông Trần Văn T, sinh năm 1959.
9. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, Đồng Nai.
10. Ông  T  ủy  quyền  cho  ông  Trần  Quốc  H  theo  văn  bản  ủy  quyền  ngày
11. 07/3/2017.
12. 6/ Ông Trần Đình P, sinh năm 1970.
13. Địa chỉ: xã C, huyện L, tỉnh Đồng Nai.
14. Ông P ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 08/3/2017.
15. 7/ Bà Trần Thị Đan Ng, sinh năm 1953.
16. Địa chỉ: Số 45 N, phường 19, quận M, TP. Hồ Chí Minh.
17. 8/ Bà Trần Thị Lệ K, sinh năm 1974.
18. Địa chỉ: Số 19B, tổ 12, khu S, thị trấn L, huyện L, Đồng Nai.
19. 9/ Bà Nguyễn Thị Th P, sinh năm 1971.
20. Địa chỉ: tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
21. Bà P ủy quyền cho ông Trần Văn T theo văn bản ủy quyền ngày 16/10/2017.
22. 10/ Chị Trần Thị Th V, sinh năm 1992.
23. 11/  Cháu  Trần  Hạo  X,  sinh  ngày  27/10/2013.  Do  chị  V  đại  diện  theo  pháp
24. 12/ Anh Trần Văn R, sinh năm 1994.
25. Địa chỉ: Số 18, tổ 7, ấp 4, xã A, huyện L, tỉnh Đồng Nai.
26. 13/ Anh Hoàng Thái Th1, sinh năm 1989.
27. 14/ Chị Hồ Thị Ngọc O, sinh năm 1988.
28. Địa chỉ: Ấp 2, xã Z, huyện L, tỉnh Đồng Nai.
29. Chị O ủy quyền cho anh Hoàng Thái Th1.
30. 15/ Ngân hàng thương mại cổ phần Y.
31. Địa chỉ: 25 bis A, phường B, quận C, TP. Hồ Chí Minh.
32. Người  đại  diện  theo  pháp  luật:  Ông  Nguyễn  Hữu  D  –  chức  vụ:  Tổng  giám
33. luật.
34. đốc.
35. Người đại diện theo ủy quyền: Anh Nguyễn Hữu S – Nhân viên ngân hàng.
36. 16/ Bà Phạm Thị E, sinh năm 1979.
37. Địa chỉ: Số 390 khu 1, thị trấn L, huyện L, tỉnh Đồng Nai.
38. Bà E ủy quyền cho ông Trần Quốc H theo văn bản ủy quyền ngày 17/11/2017.
39. (Ông Đ, ông T, ông H, ông Q, ông H1, bà N, bà Th, bà Ng, bà K, anh Th1,
40. anh S có mặt, anh R, chị V đề nghị vắng mặt).
41. NỘI DUNG VỤ ÁN:
42. -  Tại  đơn  khởi  kiện  ngày  10  tháng  02  năm  2017  và  trong  quá  trình  xét  xử,
43. nguyên đơn ông Trần Văn Đ, ông Trần Văn T trình bày:
44. Cha mẹ của hai ông là Trần Văn Q1 (Trần Văn Q1), sinh năm 1923, mất năm
45. 2007; bà Trần Thị M, sinh năm 1931, mất năm 2008. Cha mẹ của ông Q1 và bà M
46. đã mất từ lâu. Ông Q1 và bà M sinh được 15 người con, chết 04 người khi còn trẻ và
47. chưa lập gia đình, hiện giờ còn 11 người, tên là:
48. Ông Trần Văn Đ, sinh năm 1951.
49. Bà Trần Thị Đan Ng, sinh năm 1953.
50. Ông Trần Văn T, sinh năm 1959.
51. Bà Trần Thị Thúy N, sinh năm 1961.
52. Bà Trần Thị Bích Th, sinh năm 1963.
53. Ông Trần Văn T, sinh năm 1964.
54. Ông Trần Văn Q, sinh năm 1966.
55. Ông Trần Đình P, sinh năm 1970.
56. Ông Trần Quang H1, sinh năm 1972.
57. Bà Trần Thị Lệ K, sinh năm 1974.
58. Ông Trần Quốc H, sinh năm 1976.
59. Ông Q1, bà M không còn người con chung hay con riêng, con nuôi nào khác.
60. Ông Q1 và bà M để lại tài sản chung là diện tích đất 488m2 thửa đất số 101, tờ
61. bản đồ số 1 xã  A, huyện L, tỉnh Đồng Nai và tài sản gắn liền với đất. Nay là diện
62. tích đất 432,1m2 Thộc thửa 51, tờ bản đồ số 11 xã A theo bản đồ hiện trạng thửa đất
63. số 8603/2017 ngày 30/6/2017 của Văn phòng đăng ký đất đai tỉnh  Đồng Nai – chi
64. nhánh L.
65. Khi ông Q1, bà M mất thì không để lại di chúc. Tất cả anh em trong gia đình
66. có ký vào tờ thỏa thuận phân chia di sản ngày 20/7/2009 tại UBND xã A để cho ông
67. H thay mặt các anh em đứng tên quản lý, sử dụng đất nhưng không biết nội dung tờ
68. thỏa thuận là gì, vì khi ký ông H chỉ đưa cho các anh em ký vào tờ giấy trắng chứ
69. không có nội dung gì trên đó. Tuy nhiên hai ông không photo tờ giấy trắng có chữ
70. ký đó lại nên không có tài liệu để cung cấp cho Tòa án. Hai ông có nói với ông H là
71. chỉ được quản lý, sử dụng diện tích đất trên để ở và không được chuyển nhượng cho
72. người khác. Ông H cũng hứa với các anh em là chỉ ở và sẽ không chuyển nhượng.
73. Tại phiên tòa ngày 26/4/2018, hai ông thừa nhận là có biết nội dung tại tờ thỏa
74. thuận như có tại hồ sơ vụ án nhưng chỉ ký với mục đích là cho ông H đứng tên trên
75. giấy chứng nhận quyền sử dụng đất mà thôi.
76. Khi ký, tất cả các anh em đều tự nguyện, không nhầm lẫn, không bị ai lừa dối
77. hay ép buộc, đe dọa gì. Tờ thỏa thuận phân chia di sản ngày 20/7/2009 cũng không
78. phải là giả tạo để che giấu một giao dịch nào khác.
79. Hiện  nay  trên  phần  đất  đó  có  bà  Trần  Thị  Bích  Th  (độc  thân),  bà  Trần  Thị
80. Thúy N (độc thân), ông Trần Văn T (độc thân) và ông Trần Quốc H, các con của ông
81. T là Trần Văn R (độc thân), Trần Thị Th V (độc thân), con của chị V là cháu Trần
82. Hạo X đang sinh sống. Trước đây vợ cV ông T có sống trên đất này nhưng  vợ cV
83. ông đã chuyển chỗ ở sang nhà kế bên đất đang tranh chấp, còn phòng ở do ông sử
84. dụng trước đây thì hiện nay con trai là Trần Văn R đang sử dụng, còn con gái tên V
85. và cháu X thì ở chung phòng với bà Th. Trong thời gian ở trên đất thì ông T có sửa
86. chữa  nhà  nhưng  ông  không  yêu  cầu  gì,  không  yêu  cầu  giải  quyết  chi  phí  cho  việc
87. bảo quản di sản hay yêu cầu nào khác. Việc ông H thế chấp phần đất trên để vay vốn
88. ngân hàng thì hai ông không hề biết.
89. Nay ông Đ, ông T yêu cầu Tòa án phân chia di sản thừa kế của ông Q1 và bà
90. M để lại là diện tích đất 432,1m2 thửa số 51, tờ bản đồ số 11 xã  A, huyện L và tài
91. sản  gắn  liền  với  đất,  trị  giá  1.692.700.000  đồng  theo  Chứng  thư  thẩm  định  giá  số
92. 2103/TĐG-CT ngày 31/8/2017 của Công ty cổ phần thẩm định giá Đồng Nai thành
93. 11 phần bằng nhau theo giá trị. Yêu cầu để ông T nhận di sản bằng hiện vật là nhà
94. đất và thanh toán giá trị cho 10 người còn lại, mỗi người được hưởng 1/10 giá trị của
95. tài sản, tương đương với số tiền là 169.270.000 đồng. Ông Đ, ông T không yêu cầu
96. thẩm định giá lại tài sản tranh chấp, đề nghị Tòa án áp dụng chứng thư thẩm định giá
97. có tại hồ sơ vụ án để giải quyết.
98. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
99. 23/01/2017 giữa ông Trần Quốc H, bà Phạm Thị E với ông H1 Thái Th1, chị Hồ Thị
100. Ngọc O thì ông Đ, ông T không đồng ý. Tuy nhiên, hai ông không có yêu cầu gì đối
101. với hợp đồng này, việc này tự ông H và ông Th1 giải quyết. Ngoài ra, ông Đ, ông T
102. không có ý kiến và yêu cầu gì khác liên quan đến nhà đất này.
103. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, bị đơn ông
104. Trần Quốc H trình bày:
105. Ông  thống  nhất  với  lời  khai  của  nguyên  đơn  về  quan  hệ  nhân  thân  và  hàng
106. thừa kế và tài sản của cha mẹ ông là  ông Trần Văn Q1 (Trần Văn Q1) và bà Trần
107. Thị  M  để  lại.  Cha  mẹ  ông  mất  nhưng  không  để  lại  di  chúc.  Toàn  bộ  các  anh  em
108. trong gia đình đều thống nhất thỏa Thuận cho ông toàn quyền quản lý, sử dụng đối
109. với  diện  tích  đất  này,  việc  thỏa  thuận  tại  “Tờ  thỏa  thuận  phân  chia  di  sản”  ngày
110. 20/7/2009 đã được Ủy ban nhân dân xã A xác nhận, tức là quyền sử dụng đất đó là
111. tài sản của ông và ông có toàn quyền về tài sản này. Còn tài sản trên đất thì các anh
112. em trong gia đình  chưa phân chia cho ai. Khi ký tờ thỏa Thuận, tất cả các anh em
113. của ông đều tự nguyện, không nhầm lẫn, không bị ai lừa dối hay ép buộc, đe dọa gì,
114. cũng không phải là giả tạo để che giấu một giao dịch nào khác. Khi ký tờ thỏa thuận
115. trên  thì  các  anh  em  không  nói  với  ông  việc  không  được  chuyển  nhượng  quyền  sử
116. dụng đất, tại tờ thỏa thuận phân chia di sản cũng không có nội dung nào về việc ông
117. không được chuyển nhượng cho người khác.  Ông không hứa với các anh em trong
118. gia  đình  là  sẽ  không  chuyển  nhượng.  Do  đó,  ông  không  đồng  ý  với  yêu  cầu  của
119. nguyên đơn về chia đất, chỉ đồng ý chia tài sản trên đất, ông có nguyện vọng được
120. nhận  tài  sản  trên  đất  và  thanh  toán  giá  trị  lại  cho  mười  người  còn  lại.  Ngày
121. 02/4/2010,  ông kết  hôn với  chị  Châu  Ngọc  C, đến năm  2015 thì ly  hôn. Đến  ngày
122. 11/6/2016, ông kết hôn với chị Phạm Thị E.
123. Năm 2011, ông có thế chấp quyền sử dụng đất trên để vay tiền tại ngân hàng
124. HD  Bank, mục  đích vay  vốn kinh doanh, khi  ông  thế  chấp quyền sử dụng đất  ông
125. không nói với các anh em trong gia đình vì đây là đất của ông. Do không trả được nợ
126. nên ngân hàng đã kiện ông ra tòa, Tòa án đã xét xử bằng bản án và đã có hiệu lực
127. pháp luật, đã có quyết định thi hành án kê biên, xử lý tài sản nhưng chưa kê biên.
128. Phần đất trên hiện do ông Trần Văn T, bà Trần Thị Bích Th, bà Trần Thị Thúy
129. N, cháu Trần Văn R, cháu Trần Thị Th V và con của chị V là cháu Trần Hạo X và
130. ông đang quản lý, sử dụng. Sau này, ông sẽ lo chỗ ở cho các anh chị của ông là bà
131. Th, bà N, ông T là những người có tên trong hộ khẩu của ông nhưng ông không đề
132. nghị Tòa án ghi nhận trong vụ án này mà ông sẽ tự giải quyết riêng. Ông cũng không
133. hứa với bà Th như bà Th trình bày. Trong thời gian ở trên đất thì ông có sửa chữa
134. nhà  để  ở  nhưng  ông  không  yêu  cầu  gì.  Ông  không  yêu  cầu  giải  quyết  chi  phí  cho
135. việc bảo quản di sản hay yêu cầu nào khác.
136. Ông đã đăng ký cấp đổi  giấy chứng nhận  quyền sử dụng đất vào năm 2011,
137. đến  ngày  07/8/2015  mới  được  cấp  Giấy  chứng  nhận  quyền  sử  dụng  đất  số  BV
138. 102629. Hiện nay giấy này vẫn còn đang ở Ủy ban nhân dân xã A, ông chưa được
139. nhận, lý do vì sao thì ông không biết.
140. Đối  với  Hợp  đồng  đặt  cọc  và  chuyển  nhượng  quyền  sử  dụng  đất  ngày
141. 23/01/2017 giữa ông và vợ ông là bà Phạm Thị E với anh H1 Thái Th1, chị Hồ Thị
142. Ngọc O, ông không có yêu cầu gì. Đất này là của ông nên ông có quyền ký hợp đồng
143. này. Ông không đồng ý đề nghị của bà Th về việc bán 5m chiều ngang đất, phần còn
144. lại để ở vì đất là của ông thì ông có quyền bán hết để trả nợ cho ngân hàng, nếu bán
145. 5m ngang thì không đủ trả nợ cho ngân hàng.
146. - Tại các bản tự khai, biên bản hòa giải  và trong quá trình  xét xử, người có
147. quyền lợi, nghĩa vụ liên quan là các ông bà Trần Thị Đan Ng, Trần Thị Lệ K, Trần
148. Thị Bích Th, Trần Thị Thúy N, Trần Văn Q, Trần Quang H1 trình bày:
149. Các ông bà thống nhất với lời trình bày và yêu cầu của nguyên đơn. Riêng đối
150. với tờ thỏa thuận phân chia di sản lập ngày 20/7/2009 tại xã A thì các ông, bà có biết
151. nội dung của tờ thỏa thuận đã có tại hồ sơ vụ án nhưng chỉ ký với mục đích để cho
152. ông H đứng tên trên sổ đỏ thôi. Các ông bà không còn lưu giữ tờ thỏa thuận này.
153. Trong  thời  gian  ở  trên  đất  thì  bà  Th,  bà  N,  ông  T  không  sửa  chữa  hay  xây
154. thêm công trình gì trên đất nên không có yêu cầu gì, không yêu cầu giải  quyết chi
155. phí  cho việc bảo quản di  sản.  Các ông  bà  chỉ  đề nghị  Tòa  án chia thừa  kế  nhà  đất
156. như nguyên đơn yêu cầu. Ngoài ra, không có ý kiến và yêu cầu gì khác. Đối với hợp
157. đồng đặt cọc mua bán đất giữa ông H và ông Th1 thì tự hai người này giải quyết, các
158. ông bà không yêu cầu gì.
159. Riêng bà Th có trình bày thêm: Ông H có hứa sẽ cắt cho bà 1/3 diện tích đất
160. trên để ở, bà không đồng ý cho ông H chuyển nhượng quyền sử dụng đất cho người
161. khác. Tại phiên tòa ngày 20/6/2018, bà đề nghị ông H bán 5m chiều ngang đất, phần
162. còn lại để ở.
163. Bà Th, bà N cho rằng trước khi ký hợp đồng đặt cọc bán đất thì ông H ép hai
164. bà ký và hai bà có ra điều kiện là ông H phải cắt một phần đất cho hai bà ở rồi mới
165. ký. Bà Th, bà N không có chứng cứ gì về vấn đề này.
166. - Người có quyền lợi, nghĩa vụ liên quan ông Trần Văn T và Trần Đình P, bà
167. Phạm Thị E do ông Trần Quốc H là đại diện theo ủy quyền trình bày:
168. Trước đây ông P có ý kiến là đồng ý với yêu cầu khởi kiện của nguyên đơn.
169. Nhưng  sau  đó  ông  P  đã  thay  đổi  ý  kiến  và  đã  ủy  quyền  cho  ông  đến  Tòa  án  giải
170. quyết tranh chấp. Ông T, ông P xác định diện tích đất tranh chấp đã được phân chia
171. cho ông. Ông T và ông P, bà E thống nhất với ý kiến của ông. Ngoài ra, không có ý
172. kiến nào khác, ông T không yêu cầu giải quyết chi phí cho việc bảo quản di sản hay
173. yêu cầu nào khác.
174. -  Người  có  quyền  lợi,  nghĩa  vụ  liên  quan  bà  Nguyễn  Thị  Th  P  do  ông  Trần
175. Văn T là đại diện theo ủy quyền trình bày:
176. Bà P thống nhất lời trình bày của ông T.
177. - Tại các bản tự khai, người có quyền lợi, nghĩa vụ liên quan anh Trần Văn R,
178. chị Trần Thị Th V trình bày:
179. Anh, chị là con của ông Trần Văn T, anh chị không có công sức đóng góp gì
180. trên diện tích đất tranh chấp, không có ý kiến gì và hoàn toàn nhường quyền lại cho
181. ông T. Anh chị xin vắng mặt tất cả các buổi triệu tập trong quá trình giải quyết vụ án
182. cho đến khi vụ án kết thúc và có bản án có hiệu lực pháp luật.
183. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
184. quyền lợi, nghĩa vụ liên quan Ngân hàng thương mại cổ phần Y do anh Nguyễn Hữu
185. S là đại diện theo ủy quyền trình bày:
186. là  ngân  hàng)  300.000.000  đồng
187. Ngày 23/6/2011, ông H và bà Châu Ngọc C có vay tiền của ngân hàng Y (gọi tắt số
188. 00151/HĐTDNH/HDB ngày 23/6/2011. Tài sản đảm bảo là  quyền sử dụng đất đối
189. với thửa đất số 101, tờ bản đồ số 01 xã A, diện tích 488m2 (Nay là diện tích 432,1m2
190. Thộc  thửa  số  51,  tờ  bản  đồ  số  27  xã  A)  theo  Hợp  đồng  thế  chấp  tài  sản  số
191. 00151/HĐTC/HDB ngày 23/6/2011, hợp đồng đã được công chứng, chứng thực tại
192. UBND  xã  A,  huyện  L,  tỉnh  Đồng  Nai,  đăng  ký  giao  dịch  bảo  đảm  tại  Phòng  tài
193. nguyên và môi trường huyện L, tỉnh Đồng Nai vào ngày 23/6/2011.
194. theo  Hợp  đồng
195. tín  dụng
196. Trong quá trình thực hiện hợp đồng, ông H và bà C đã vi phạm nghĩa vụ trả
197. nợ nên Ngân hàng đã khởi kiện ông H và bà C ra Tòa án nhân dân huyện L. Ngày
198. 16/7/2012,  Tòa  án  đã  xét  xử  bằng  bản  án  số  04/2012/KDTM-ST  ngày  16/7/2012,
199. buộc ông H và bà C phải thanh toán nợ cho ngân hàng. Tài sản thế chấp là quyền sử
200. dụng đất đối với thửa đất số 101, tờ bản đồ số 01, tổng diện tích 488m2 được đảm
201. bảo thi hành án.
202. Ngày  27/11/2013,  chi  cục  thi  hành  án  dân  sự  huyện  L  đã  ra  quyết  định  kê
203. biên, xử lý tài sản số 50/QĐ-CCTHA ngày 14/4/2014. Hiện nay cơ quan thi hành án
204. vẫn đang tiến hành thi hành bản án số 04 nêu trên của Tòa án nhưng chưa kê biên,
205. xử lý tài sản thế chấp do đang có tranh chấp.
206. Nay Ngân hàng đề nghị Tòa án xem xét, giải quyết vụ án theo đúng quy định
207. pháp luật để Chi cục thi hành án dân sự huyện L, tỉnh Đồng Nai tiếp tục thi hành bản
208. án số 04 nêu trên để bảo vệ quyền, lợi ích hợp pháp cho Ngân hàng.
209. - Tại các bản tự khai, biên bản hòa giải và trong quá trình xét xử, người có
210. quyền lợi, nghĩa vụ liên quan anh H1 Thái Th1 trình bày:
211. Yêu cầu Tòa án giải quyết vụ án theo pháp luật, anh và vợ anh là chị O không
212. có ý kiến gì đối với yêu cầu của nguyên đơn. Đối với Hợp đồng đặt cọc và chuyển
213. nhượng quyền sử dụng đất ngày 23/01/2017 giữa vợ chồng anh và vợ chồng anh H,
214. anh chị sẽ đợi Tòa án giải  quyết xong vụ án tranh chấp thừa kế này rồi sẽ tiếp tục
215. giao  dịch  mua  bán  đất.  Hợp  đồng  đặt  cọc  này  được  ký  tại  nhà  đất  mà  đang  tranh
216. chấp trong vụ án này và có những người anh em của ông H đã ký tên làm chứng vào
217. hợp đồng, khi ký thì những người này vui vẻ, không bị ai ép buộc gì.
218. - Ý kiến phát biểu của đại diện Viện kiểm sát nhân dân huyện Long Thành:
219. Tại phiên tòa, đại diện Viện kiểm sát nhân dân huyện Long Thành phát biểu ý
220. kiến  về  việc  tuân  theo  pháp  luật  của  Thẩm  phán,  Hội  đồng  xét  xử  được  thực  hiện
221. đúng theo quy định của Bộ luật tố tụng dân sự từ khi Tòa án thụ lý vụ án đến khi Hội
222. đồng  xét xử  vào  phòng nghị  án. Việc  chấp  hành  pháp  luật  của  các  đương  sự  được
223. thực hiện theo quy định của Bộ luật Tố tụng dân sự.
224. Về việc giải quyết vụ án: Về nguồn gốc tài sản đang tranh chấp gồm có quyền
225. sử dụng diện tích đất 432,1m2 thuộc thửa số 51, tờ bản đồ số 11, xã A và tài sản gắn
226. liền với đất có nguồn gốc là do ông Q1, bà M tạo lập ra. Vào năm 2007 ông Q1 chết,
227. năm 2008 bà M chết và không để lại di chúc, các bên đương sự thống nhất thừa nhận
228. sự việc này. Ngày 20/7/2009, mười một anh em trong gia đình ông Đ, ông T, ông H
229. lập tờ thỏa thuận phân chia di sản thừa kế có xác nhận của Ủy ban nhân dân xã  A.
230. Tại tờ thỏa thuận này mười một anh em trong gia đình đã phân chia diện tích đất nêu
231. trên cho ông H toàn quyền quản lý, sử dụng trên cơ sở tự nguyện, không bị ép buộc, đe dọa, không trái pháp luật và đạo đức xã hội. Việc ông Đ, ông T cho rằng các anh chị em trong gia đình chỉ thống nhất giao diện tích đất nêu trên cho ông H thay mặt các  anh  chị  em  đi đăng  ký kê  khai  cấp  đổi giấy  chứng nhận  quyền  sử dụng đất và đứng tên giấy chứng nhận, chỉ giao cho ông H nhà đất để ở và không được chuyển nhượng  cho  người  khác,  chứ  không  cho  ông  H  toàn  bộ  tài  sản  do  cha  …
232. Riêng đối với tài sản là các căn nhà và công trình trên đất, các bên  đương sự đều thừa nhận là tài sản do cha mẹ chết để lại, tại thời điểm lập tờ thỏa thuận phân chia  di sản thừa  kế  các  bên đương sự  chưa  thỏa thuận phân chia, chưa  giao  quyền quản lý, sử dụng và định đoạt các tài sản này. Cụ thể, hiện tại trên đất có bà N, ông T, ông H, bà Th, các con của ông T là R, V đang quản lý, sử dụng các căn nhà do cha mẹ của ông Đ, ông T, ông H đã xây dựng trước đó. Do đó, tài sản này là được …
233. xem xét quyết định.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
2. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
3. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
4. [BLDS 2015] Điều 623. Thời hiệu thừa kế. 1. Thời hiệu để người thừa kế yêu cầu chia di sản là 30 năm đối với bất động sản, 10 năm đối với động sản, kể từ thời điểm mở thừa kế. Hết thời hạn này thì di sản thuộc về người thừa kế đang quản lý di sản đó. Trường hợp không có người thừa kế đang quản lý di sản thì di sản được giải quyết như sau: a) Di sản thuộc quyền sở hữu của người đang chiếm hữu theo quy định tại Điều 236 của Bộ luật này; b) Di sản thuộc về Nhà nước, nếu không có người chiếm hữu quy định tại điểm a khoản này. 2. Thời hiệu để người thừa kế yêu cầu xác nhận quyền thừa kế của mình hoặc bác bỏ quyền thừa kế của người khác là 10 năm, kể từ thời điểm mở thừa kế. 3. Thời hiệu yêu cầu người thừa kế thực hiện
5. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
Assuming these hypotheses are true in this case:
Thời hiệu thừa kế: Theo Điều 623 BLDS 2015, thời hiệu yêu cầu chia di sản đối với bất động sản là 30 năm kể từ thời điểm mở thừa kế.
According to the given rules and hypotheses, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá yêu cầu của nguyên đơn, chúng ta cần phân tích từng yếu tố:

1. **Thời hiệu thừa kế**: Theo Điều 623 BLDS 2015, thời hiệu yêu cầu chia di sản đối với bất động sản là 30 năm kể từ thời điểm mở thừa kế. Theo đơn khởi kiện, thời điểm mở thừa kế là năm 2007 (khi ông Trần Văn Q và bà Trần Thị M mất). Như vậy, thời hiệu yêu cầu chia di sản đã hết vào năm 2037.

2. **Phân chia di sản theo pháp luật**: Theo Điều 660 BLDS 2015, khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản. Tuy nhiên, trong vụ án này không có thông tin về việc có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra.

3. **Phân chia di sản theo di chúc**: Theo Điều 659 BLDS 2015, nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc. Trong vụ án này, không có thông tin về việc có di chúc.

4. **Phân chia di sản theo thỏa thuận**: Theo Điều 662 BLDS 2015, nếu đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận. Trong vụ án này, thỏa thuận phân chia di sản đã được lập vào năm 2009, trước khi thời hiệu yêu cầu chia di sản hết vào năm 2037.

Như vậy, yêu cầu của nguyên đơn về việc phân chia di sản theo thỏa thuận đã được lập trước thời hiệu yêu cầu chia di sản, và thỏa thuận này đã được các bên thừa nhận. Tuy nhiên, yêu cầu của nguyên đơn về việc chia tài sản bằng hiện vật (nhà đất) không phù hợp với quy định tại Điều 660 BLDS 2015 vì không có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra.

Kết luận: Yêu cầu của nguyên đơn được chấp nhận một phần. Yêu cầu về việc chia tài sản bằng hiện vật được chấp nhận, nhưng yêu cầu về việc chia tài sản theo thỏa thuận được lập trước thời hiệu yêu cầu chia di sản không được chấp nhận.
```

## Result
- outcome: **the court rejects all of the plaintiff's claims**
- converged: False
- accepted hypotheses:
  - Thời hiệu thừa kế: Theo Điều 623 BLDS 2015, thời hiệu yêu cầu chia di sản đối với bất động sản là 30 năm kể từ thời điểm mở thừa kế.