# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Trong  Đơn  khởi  kiện  ngày  18  tháng  6  năm  2013,  Đơn  khởi  kiện  bổ  sung ngày 08/10/2013, yêu cầu bổ sung đơn khởi kiện tại phiên tòa sơ thẩm ngày 02/12/ 2015 và  quá trình  tham  gia  tố  tụng  tại  Tòa  án,  nguyên  đơn  là ông  Nguyễn  Văn T trình bày: Ông được mẹ đẻ là cụ Phạm Thị M chia cho mảnh đất thổ cư có diện tích hơn 1.000 m2, vị trí phía Đông giáp thửa đất nhà bà Trần Thị V, phía Đông Bắc giáp đất ông Nguyễn Trọng C, phía Tây Bắc giáp kênh thoát nước, phía Tây Nam giáp đất …
2. Năm 1992, ông đã thế chấp mảnh đất và toàn bộ tài sản trên đất để vay tiền Ngân hàng N (sau đây gọi tắt là Ngân hàng NN&PTNT) chi nhánh K, Hải Phòng với  số  tiền  là  9.500.000  đồng và  26.000.000  đồng  tiền  vay  EC.  Có  xác  nhận  của UBND xã Bắc Hà, K.
3. Năm 1994, do gặp thiên tai lũ lụt, toàn bộ cá tôm trong đầm bị mất hết, gia đình ông không có khả năng thanh toán khoản vay của Ngân hàng. Năm 1997 ông phải vào thành phố Hồ Chí Minh tìm việc làm, chỉ còn lại mẹ ông là cụ Phạm Thị M và vợ ông là bà Trịnh Thị T V ở nhà.
4. Năm 2007, ông trở về nhà thì diện tích đất thổ cư cũng như đất canh tác và toàn bộ tài sản hợp pháp của gia đình ông đã bị gia đình cụ Phạm Văn L chiếm giữ bất  hợp  pháp.  Ông  không  có bất  kỳ  một  thỏa  thuận  nào  về  việc  chuyển  nhượng quyền  sử  dụng  đất  nêu  trên,  mặt khác  các  giấy  tờ  liên  quan  đến  thửa  đất  này  vẫn được lưu giữ tại Ngân hàng, khoản nợ của ông vẫn chưa được thanh toán.
5. Việc chiếm giữ bất hợp pháp của cụ Phạm Văn L và con trai là ông Phạm Văn Th cùng con dâu là bà Vũ Thị H đối với thửa đất mà gia đình ông là chủ sử dụng hợp pháp và hiện đang thế chấp tại Ngân hàng là không có căn cứ pháp luật. Việc ông Th, bà H cho rằng đã nhận chuyển nhượng diện tích nhà, đất này mà ông không được biết là trái quy định của pháp luật.
6. Các tài liệu, chứng cứ để chứng minh cho yêu cầu khởi kiện ông T, bà V nộp cho Tòa án gồm: Bản tường trình chia đất của bà Phạm Thị M; Biên bản xác định ranh giới giữa ông C và ông T có sơ đồ kèm theo; ảnh chụp nhà ông T; hồ sơ thế chấp quyền sử dụng đất và tài sản gắn liền với đất; tài liệu về nguồn gốc đất và Biên bản hòa giải giải quyết tranh chấp của UBND phường P; Biên lai gửi tiền cho ông T ngày 02/3/2001.
7. Người có quyền lợi, nghĩa vụ liên quan và là người kế thừa quyền và nghĩa vụ của nguyên đơn là bà Trịnh Thị T V khai: Bà về làm dâu từ năm 1978 và được nghe cụ M nói lại là vào khoảng năm 1973; 1974 cụ M đã chia đất của ông cha để lại cho 02 con là ông C và ông T. Trên phần đất của ông T được chia đến năm 1989 ông T và bà đã xây 01 căn nhà 02 tầng. Năm 1990, ông T thế chấp nhà 02 tầng trên cho Ngân hàng để vay tiền làm kinh tế. Tuy nhiên việc làm ăn thua lỗ năm 1997 ông T vào thành phố Hồ Chí …
8. Lời khai của bà Trịnh Thị T V, chị Nguyễn Thị Mai A và anh Nguyễn Trong Tuấn là người kế thừa quyền và nghĩa vụ của nguyên đơn thống nhất với nhau như sau:
9. Diện tích đất thổ cư, đất canh tác, nhà ở và các tài sản trên đất mà hiện nay ông Th, bà H đang quản lý sử dụng có nguồn gốc của ông cha để lại đúng là đất và tài sản gắn liền với đất mà cụ M và cụ L đã giao dịch với nhau và cũng là nhà ở 02 tầng và tài sản gắn liền với đất thổ cư mà ông T đã thế chấp để vay tiền Ngân hàng. Theo hồ sơ vay tiền Ngân hàng thì diện tích đất nêu trên là thửa số 905 tờ bản đồ số 01 cũng chính là phần đất và tài sản mà hiện nay gia đình chúng tôi đang tranh chấp với …
10. Nay  người  kế  thừa  quyền,  nghĩa  vụ  của  nguyên  đơn  yêu  cầu  Tòa  án  giải quyết:
11. - Tuyên bố hợp đồng mua bán nhà, đất giữa cụ Phạm Văn L và cụ Phạm Thị M là vô hiệu.
12. - Buộc ông Phạm Văn Th và bà Vũ Thị H phải trả lại diện tích nhà và đất kể trên cho nguyên đơn.
13. Tại phiên tòa ngày 23/4/2021, người kế thừa quyền, nghĩa vụ của nguyên đơn bổ sung yêu cầu khởi kiện bao gồm:
14. - Yêu cầu tuyên bố vô hiệu đối với giao dịch chuyển nhượng quyền sở hữu tài sản và quyền sử dụng đất giữa cụ L với ông Th, bà H;
15. - Yêu cầu hủy giấy chứng nhận quyền sử dụng đất số S: 801530 ngày 15/3/2002 của UBND quận K cấp cho ông Phạm Văn Th và bà Vũ Thị H;
16. - Yêu cầu định giá lại tài sản tranh chấp vì thời gian định giá đã quá 6 tháng;
17. Bị đơn là bà Vũ Thị H trình bày: Năm 1999 cụ Phạm Văn L là bố chồng bà và là bố đẻ của ông Phạm Văn Th có mua một mảnh đất bao gồm nhà, ao, vườn và 03 sào đất canh tác của cụ Phạm Thị M là mẹ đẻ ông T và bà Trịnh Thị T V là vợ ông T với số tiền là 28.000.000 đồng. Cụ M có làm thủ tục giấy tờ mua bán viết tay cho cụ L, cụ Phạm Văn L giao tiền tại nhà ông Trần Văn Th (nguyên là trưởng khu dân cư Đồng Tử 2) có sự chứng kiến của bà Trịnh Thị T V, bà Phạm Thị B và ông Th. Số tiền  đó  bà  bà  Trịnh  …
18. Ngày 15/3/2002, vợ chồng bà đã được UBND quận K cấp Giấy chứng nhận quyền sử dụng đất (sau đây viết tắt là GCNQSDĐ) số S: 801530 với diện tích 910 m2, mục đích sử dụng “2 lúa”, thời hạn sử dụng đến năm 2020 tại thửa đất trên mà cụ L đã nhận chuyển nhượng của cụ M, bà V.
19. Ngày 03/8/2004, cụ L tiếp tục xác lập đơn đề nghị về việc xin xác nhận thị thực hành chính trong lĩnh vực giao dịch dân sự về nhà ở, đất ở có xác nhận của UBND phường P, K chuyển quyền sử dụng toàn bộ nhà và diện tích đất thổ cư 1.303 m2 tại thửa đất mà cụ L đã nhận chuyển nhượng của cụ M và bà V.
20. Ngày 04/8/2004, UBND phường P, quận K đã lập trích đo thửa đất dùng cho việc đăng ký kê khai sử dụng đất thửa đất số 128, tờ bản đồ số 3000591 -7-(15), tại tổ 4 khu dân cư Đồng Tử 2, phường P, quận K, thành phố Hải Phòng với diện tích 1.303 m2 mang tên vợ chồng bà là Phạm Văn Th và Vũ Thị H.
21. Mọi thủ tục giấy tờ mua bán, hồ sơ cấp giấy chứng nhận quyền sử dụng đất vợ chồng bà và cụ L đã chuyển cho UBND phường P, do cụ Phạm Văn L đã chết nên mọi giấy tờ mua bán giữa cụ M và cụ L vợ chồng bà không tìm thấy.
22. Việc mua bán giữa cụ M và cụ L, ông T và bà V đều biết và không có ý kiến gì. Cụ L đã nhận nhà, đất sử dụng và đã xây dựng nhà xưởng sản xuất, xây tường bao, bờ rào sử dụng trong suốt thời gian từ năm 2001 đến năm 2011 ông T mới có đơn đề nghị UBND phường P giải quyết. Bà H cho rằng việc mua bán nhà, đất giữa cụ L và cụ M là hợp pháp và vợ chồng bà sử dụng từ năm 2001 đến nay không có việc chiếm giữ bất hợp pháp như ông Nguyễn Văn T khai. Vợ chồng bà không đồng ý trả lại nhà và đất ở, đất canh …
23. Tài liệu, chứng cứ để chứng minh cho yêu cầu của mình, bà H nộp cho Tòa án gồm:  Giấy  chứng  nhận  quyền  sử  dụng  đất  số  S:  801530;  Biên  bản  xác  định  ranh giới, mốc giới thửa đất, Trích đo thửa đất để đăng ký kê khai sử dụng đất của UBND phường P cấp cho ông Th, bà H; Đơn đề nghị xin xác nhận giao dịch dân sự về nhà ở,  đất  ở  của  cụ  L  chuyển  quyền  cho  ông  Th,  bà  H;  các  Hợp  đồng,  giấy  tờ  nhận chuyển nhượng QSDĐ của gia đình cụ L với bà Trần Thị Nhinh, bà Trần Thị …
24. Đại diện Ngân hàng NN&PTNT Chi nhánh K (nay là Ngân hàng NN&PTNT Việt  Nam,  Chi  nhánh  quận  K  Đông  Hải  Phòng)  trình  bày:  Tháng  3/1992  ông Nguyễn Văn T có thế chấp tài sản là 01 nhà ở 02 tầng đất 90 m2 và 02 mẫu đầm hồ tại thửa số 905, tờ bản đồ số 01 thuộc xứ Đồng Tử, chỉ giới giáp thửa 933+934, phía Tây  giáp  thửa  988,  phía  Bắc  giáp  thửa  931,  phía  Đông giáp  thửa  902  để đảm  bảo cho hai khoản vay 9.500.000 đồng và EC 26.000.000 đồng, có xác nhận của UBND xã Bắc Hà (BL 19).
25. Năm  2012,  ông  T  đã  thanh  toán  10.000.000  đồng  đối  với  khoản  vay 9.500.000 đồng (trong đó tiền gốc là 9.450.000 đồng, tiền lãi là 550.000 đồng). Đối với khoản vay EC đến nay đã được xóa nợ.   Tính đến ngày 11/5/2021, khoản vay của ông T còn nợ tiền gốc là 50.000.000 đồng, tiền lãi là 9.888.000 đồng, cộng bằng 9.938.000  đồng.  Đại  diện  Ngân  hàng  yêu  cầu  ai  là  người  được  sở  hữu  tài  sản  thế chấp thì phải trả số tiền nêu trên.
26. Tại phiên hòa giải ngày 12 tháng 3 năm 2021 bà V và chị Mai A tự nguyện trả nợ Ngân hàng số tiền nêu trên. Tại phiên tòa bà  V khai tiền nợ Ngân hàng là của gia đình bà, nhưng tài sản thế chấp chưa biết ai được sở hữu cho nên bà chưa có ý kiến về việc này.
27. Người kế thừa quyền nghĩa vụ của nguyên đơn là chị Nguyễn Thị Lan trình bày: Chị là con riêng của ông T, nhưng từ nhỏ chị và ông T không có trách nhiệm gì với nhau, nay chị từ chối tham gia tố tụng. Bà V, chị Mai A, anh Tuấn cũng cho rằng chị Lan không liên quan gì đến vụ việc.
28. Người kế thừa quyền nghĩa vụ của bị đơn bà Phạm Thị T và ông Phạm Văn V, chị Nguyễn Thị L trình bày thống nhất với nhau như sau:
29. Khi  cụ  Phạm  Văn  L  còn  sống,  đã  mua  nhà,  đất  của  cụ  Phạm  Thị  M,  Hợp đồng  chuyển  nhượng  quyền  sở  hữu  nhà  và  sử  dụng  đất  được  viết  giấy  có  người làm chứng.  Cụ  M  đã  nhận  đủ  tiền,  cụ  L  đã  nhận  nhà, đất  và  sử  dụng  ổn  định  từ năm 2001 đến năm 2002 thì cụ L viết giấy chuyển nhượng quyền sử dụng đất nông nghiệp là 910 m2 cho vợ chồng ông Phạm Văn Th và bà Vũ Thị H. Ông Th, bà H đã  được  UBND  quận  K  cấp  giấy  chứng nhận  quyền  sử  dụng (GCNQSD)  đất  …
30. Lời khai của người làm chứng:
31. Ông Trần Văn Th trình bày: Năm 1999-2000, ông là Trưởng khu dân cư Đồng Tử 2 phường P, quận K. Ông được biết cụ M có ý định bán nhà, đất từ rất lâu, sau đó có cụ L đến mua. Hai bên đã thống nhất ra chính quyền làm thủ tục chuyển nhượng, cùng thời điểm đó cụ M có chia đất cho ông C và ông T, mục đích cụ M chia đất cho ông C là để cụ M và bà V bán phần nhà, đất của ông T. Cụ M và bà V vợ ông T đã bán phần đất của ông T cho cụ L với giá khoảng 29 triệu hay 39 triệu ông không nhớ cụ thể, trên đất …
32. Bà Phạm Thị B trình bày: Nguồn gốc đất ông T đang tranh chấp bà không biết của ai, chỉ thấy cụ M bảo bà ra chứng kiến việc trả tiền giữa cụ L và cụ M cùng với bà V (vợ ông T), tại nhà ông Th (cụm trưởng lúc đó) là tiền bán nhà và đất. Cụ L giao cho cụ M 28 triệu đồng, cụ M đưa cho bà V 20 triệu đồng, còn 8 triệu đồng cụ M để lại mua vàng. Bà V (vợ ông T) cùng với bà V (vợ ông Th) lai nhau đi gửi tiền cho ông T, lúc ở nhà bà nghe cụ M nói gửi tiền vào miền Nam cho ông T. Việc bán nhà và đất chủ …
33. Ông Trần Huy C trình bày: Nguồn gốc đất của ông T là do bố mẹ để lại đất thổ cư, tại hồ sơ của UBND phường quản lý có tên của cụ Phạm Thị M, không có tên ông T. Ông T chỉ có hợp đồng thuê đất đầm 5% ở gần nhà ông. Sau khi ông T đi khỏi địa phương UBND phường P đã thu hồi và hủy Hợp đồng thuê đất và ký hợp đồng cho người khác sử dụng, đất 5% này là đất công ích của địa phương… Trong bản xác định ranh  giới  ngày  01/10/1999  là  do  gia  đình  cụ  M  lập  ông  chỉ  chứng  kiến,  sau  đó  gia …
34. Các lời trình bày của ông Nguyễn Anh Văn, Nguyễn Văn Th, Trần Văn Cửu, Lê Sơn Hải, bà Nguyễn Thị Phiên (BL 182 đến 187), bà Nguyễn Thị Loan (BL 189) đều khẳng định nguồn gốc nhà và đất của ông T là của bố mẹ để lại và chỉ nghe kể lại là cụ M và bà V có bán nhà cho cụ L. Lời khai của ông Nguyễn Văn Hễ thì trong thời gian chưa bán nhà, bà V vợ ông T hàng ngày thúc dục cụ M bán nhà để gửi tiền cho ông T. Sau khi bán nhà xong cụ M vào miền Nam một thời gian rồi về thì ở nhà ông Hễ (cạnh nhà cụ M đã …
35. Ý kiến của người bảo vệ quyền và lợi ích hợp pháp của nguyên đơn:
36. Các đương sự và người làm chứng đều xác định  cụ M đã giao dịch chuyển nhượng quyền sử dụng đất và tài sản gắn liền với đất cho cụ L. Bà V đã gửi tiền cho ông T ở thành phố Hồ Chí Minh là có thật. Tuy nhiên, năm 1999 cụ M đã chia đất cho hai người con là ông C và ông T, ông T được sử dụng phần đất có nhà và các công trình phụ do ông T và bà V xây dựng là tài sản của ông T và bà V. Bà V không thể hiện ý chí bán nhà cho cụ L. Việc ông T điện đàm về nhà ông Hài nhờ ông Th bán nhà là có thật, xong …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 129. Giao dịch dân sự vô hiệu do không tuân thủ quy định về hình thức. Giao dịch dân sự vi phạm quy định điều kiện có hiệu lực về hình thức thì vô hiệu, trừ trường hợp sau đây: 1. Giao dịch dân sự đã được xác lập theo quy định phải bằng văn bản nhưng văn bản không đúng quy định của luật mà một bên hoặc các bên đã thực hiện ít nhất hai phần ba nghĩa vụ trong giao dịch thì theo yêu cầu của một bên hoặc các bên, Tòa án ra quyết định công nhận hiệu lực của giao dịch đó; 2. Giao dịch dân sự đã được xác lập bằng văn bản nhưng vi phạm quy định bắt buộc về công chứng, chứng thực mà một bên hoặc các bên đã thực hiện ít nhất hai phần ba nghĩa vụ trong giao dịch thì theo yêu cầu của một bên hoặc các bên, Tò
3. [BLDS 2015] Điều 73. Huỷ bỏ quyết định tuyên bố chết. 1. Khi một người bị tuyên bố là đã chết trở về hoặc có tin tức xác thực là người đó còn sống thì theo yêu cầu của người đó hoặc của người có quyền, lợi ích liên quan, Tòa án ra quyết định huỷ bỏ quyết định tuyên bố người đó là đã chết. 2. Quan hệ nhân thân của người bị tuyên bố là đã chết được khôi phục khi Tòa án ra quyết định hủy bỏ quyết định tuyên bố người đó là đã chết, trừ trường hợp sau đây: a) Vợ hoặc chồng của người bị tuyên bố là đã chết đã được Tòa án cho ly hôn theo quy định tại khoản 2 Điều 68 của Bộ luật này thì quyết định cho ly hôn vẫn có hiệu lực pháp luật; b) Vợ hoặc chồng của người bị tuyên bố là đã chết đã kết hôn với người khác thì việc k
4. [BLDS 2015] Điều 531. Hình thức hợp đồng vận chuyển tài sản. 1. Hợp đồng vận chuyển tài sản được giao kết bằng văn bản, bằng lời nói hoặc được xác lập bằng hành vi cụ thể. 2. Vận đơn hoặc chứng từ vận chuyển tương đương khác là bằng chứng của việc giao kết hợp đồng giữa các bên
5. [BLDS 2015] Điều 51. Giám sát việc giám hộ. 1. Người thân thích của người được giám hộ thỏa thuận cử người giám sát việc giám hộ trong số những người thân thích hoặc chọn cá nhân, pháp nhân khác làm người giám sát việc giám hộ. Việc cử, chọn người giám sát việc giám hộ phải được sự đồng ý của người đó. Trường hợp giám sát việc giám hộ liên quan đến quản lý tài sản của người được giám hộ thì người giám sát phải đăng ký tại Ủy ban nhân dân cấp xã nơi cư trú của người được giám hộ. Người thân thích của người được giám hộ là vợ, chồng, cha, mẹ, con của người được giám hộ; nếu không có ai trong số những người này thì người thân thích của người được giám hộ là ông, bà, anh ruột, chị ruột, em ruột của người được giám h
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Dựa trên các quy định được cung cấp và các thông tin về vụ kiện đã cung cấp, tôi sẽ phân tích từng yêu cầu của nguyên đơn:

1. Yêu cầu tuyên bố hợp đồng mua bán nhà, đất giữa cụ Phạm Văn L và cụ Phạm Thị M là vô hiệu:
- Theo Điều 129 BLDS 2015, giao dịch dân sự vô hiệu do không tuân thủ quy định về hình thức. 
- Tuy nhiên, theo Điều 651 BLDS 2015, người thừa kế theo pháp luật là bà Phạm Thị T V, không phải là cụ Phạm Thị M. 
- Do đó, bà Phạm Thị T V không có quyền yêu cầu tuyên bố hợp đồng vô hiệu.

2. Yêu cầu ông Phạm Văn Th và bà Vũ Thị H trả lại diện tích nhà và đất:
- Theo Điều 651 BLDS 2015, người thừa kế theo pháp luật là bà Phạm Thị T V.
- Bà Phạm Thị T V không có quyền yêu cầu ông Th và bà H trả lại đất, nhà vì bà không phải là người thừa kế hợp pháp.

3. Yêu cầu hủy giấy chứng nhận quyền sử dụng đất:
- Cũng như yêu cầu trả lại đất, nhà, giấy chứng nhận quyền sử dụng đất cũng không thể được hủy bởi bà Phạm Thị T V.
- Bà Phạm Thị T V không phải là người thừa kế hợp pháp.

4. Yêu cầu định giá lại tài sản tranh chấp:
- Không có quy định pháp luật cho phép định giá lại tài sản khi đã quá 6 tháng kể từ ngày cấp giấy chứng nhận quyền sử dụng đất.
- Việc này không phù hợp với quy định tại Điều 531 BLDS 2015.

5. Yêu cầu tuyên bố vô hiệu giao dịch chuyển nhượng quyền sở hữu tài sản và quyền sử dụng đất giữa cụ L với ông Th, bà H:
- Đây là yêu cầu liên quan đến giao dịch giữa cụ L và ông Th, bà H, không liên quan trực tiếp đến bà Phạm Thị T V.
- Bà Phạm Thị T V không có quyền yêu cầu tuyên bố giao dịch vô hiệu.

Tóm lại, yêu cầu của nguyên đơn không được chấp nhận toàn bộ. Chỉ có một yêu cầu có thể được chấp nhận là việc định giá lại tài sản (nếu được chấp nhận, nhưng không chắc chắn vì đã quá 6 tháng kể từ ngày cấp giấy chứng nhận quyền sử dụng đất).

Yêu cầu của nguyên đơn không được chấp nhận (toàn bộ).
```

## A.2#1 — abductive (plaintiff)

**Prompt**
```
Considering the following facts:
1. Trong  Đơn  khởi  kiện  ngày  18  tháng  6  năm  2013,  Đơn  khởi  kiện  bổ  sung ngày 08/10/2013, yêu cầu bổ sung đơn khởi kiện tại phiên tòa sơ thẩm ngày 02/12/ 2015 và  quá trình  tham  gia  tố  tụng  tại  Tòa  án,  nguyên  đơn  là ông  Nguyễn  Văn T trình bày: Ông được mẹ đẻ là cụ Phạm Thị M chia cho mảnh đất thổ cư có diện tích hơn 1.000 m2, vị trí phía Đông giáp thửa đất nhà bà Trần Thị V, phía Đông Bắc giáp đất ông Nguyễn Trọng C, phía Tây Bắc giáp kênh thoát nước, phía Tây Nam giáp đất …
2. Năm 1992, ông đã thế chấp mảnh đất và toàn bộ tài sản trên đất để vay tiền Ngân hàng N (sau đây gọi tắt là Ngân hàng NN&PTNT) chi nhánh K, Hải Phòng với  số  tiền  là  9.500.000  đồng và  26.000.000  đồng  tiền  vay  EC.  Có  xác  nhận  của UBND xã Bắc Hà, K.
3. Năm 1994, do gặp thiên tai lũ lụt, toàn bộ cá tôm trong đầm bị mất hết, gia đình ông không có khả năng thanh toán khoản vay của Ngân hàng. Năm 1997 ông phải vào thành phố Hồ Chí Minh tìm việc làm, chỉ còn lại mẹ ông là cụ Phạm Thị M và vợ ông là bà Trịnh Thị T V ở nhà.
4. Năm 2007, ông trở về nhà thì diện tích đất thổ cư cũng như đất canh tác và toàn bộ tài sản hợp pháp của gia đình ông đã bị gia đình cụ Phạm Văn L chiếm giữ bất  hợp  pháp.  Ông  không  có bất  kỳ  một  thỏa  thuận  nào  về  việc  chuyển  nhượng quyền  sử  dụng  đất  nêu  trên,  mặt khác  các  giấy  tờ  liên  quan  đến  thửa  đất  này  vẫn được lưu giữ tại Ngân hàng, khoản nợ của ông vẫn chưa được thanh toán.
5. Việc chiếm giữ bất hợp pháp của cụ Phạm Văn L và con trai là ông Phạm Văn Th cùng con dâu là bà Vũ Thị H đối với thửa đất mà gia đình ông là chủ sử dụng hợp pháp và hiện đang thế chấp tại Ngân hàng là không có căn cứ pháp luật. Việc ông Th, bà H cho rằng đã nhận chuyển nhượng diện tích nhà, đất này mà ông không được biết là trái quy định của pháp luật.
6. Các tài liệu, chứng cứ để chứng minh cho yêu cầu khởi kiện ông T, bà V nộp cho Tòa án gồm: Bản tường trình chia đất của bà Phạm Thị M; Biên bản xác định ranh giới giữa ông C và ông T có sơ đồ kèm theo; ảnh chụp nhà ông T; hồ sơ thế chấp quyền sử dụng đất và tài sản gắn liền với đất; tài liệu về nguồn gốc đất và Biên bản hòa giải giải quyết tranh chấp của UBND phường P; Biên lai gửi tiền cho ông T ngày 02/3/2001.
7. Người có quyền lợi, nghĩa vụ liên quan và là người kế thừa quyền và nghĩa vụ của nguyên đơn là bà Trịnh Thị T V khai: Bà về làm dâu từ năm 1978 và được nghe cụ M nói lại là vào khoảng năm 1973; 1974 cụ M đã chia đất của ông cha để lại cho 02 con là ông C và ông T. Trên phần đất của ông T được chia đến năm 1989 ông T và bà đã xây 01 căn nhà 02 tầng. Năm 1990, ông T thế chấp nhà 02 tầng trên cho Ngân hàng để vay tiền làm kinh tế. Tuy nhiên việc làm ăn thua lỗ năm 1997 ông T vào thành phố Hồ Chí …
8. Lời khai của bà Trịnh Thị T V, chị Nguyễn Thị Mai A và anh Nguyễn Trong Tuấn là người kế thừa quyền và nghĩa vụ của nguyên đơn thống nhất với nhau như sau:
9. Diện tích đất thổ cư, đất canh tác, nhà ở và các tài sản trên đất mà hiện nay ông Th, bà H đang quản lý sử dụng có nguồn gốc của ông cha để lại đúng là đất và tài sản gắn liền với đất mà cụ M và cụ L đã giao dịch với nhau và cũng là nhà ở 02 tầng và tài sản gắn liền với đất thổ cư mà ông T đã thế chấp để vay tiền Ngân hàng. Theo hồ sơ vay tiền Ngân hàng thì diện tích đất nêu trên là thửa số 905 tờ bản đồ số 01 cũng chính là phần đất và tài sản mà hiện nay gia đình chúng tôi đang tranh chấp với …
10. Nay  người  kế  thừa  quyền,  nghĩa  vụ  của  nguyên  đơn  yêu  cầu  Tòa  án  giải quyết:
11. - Tuyên bố hợp đồng mua bán nhà, đất giữa cụ Phạm Văn L và cụ Phạm Thị M là vô hiệu.
12. - Buộc ông Phạm Văn Th và bà Vũ Thị H phải trả lại diện tích nhà và đất kể trên cho nguyên đơn.
13. Tại phiên tòa ngày 23/4/2021, người kế thừa quyền, nghĩa vụ của nguyên đơn bổ sung yêu cầu khởi kiện bao gồm:
14. - Yêu cầu tuyên bố vô hiệu đối với giao dịch chuyển nhượng quyền sở hữu tài sản và quyền sử dụng đất giữa cụ L với ông Th, bà H;
15. - Yêu cầu hủy giấy chứng nhận quyền sử dụng đất số S: 801530 ngày 15/3/2002 của UBND quận K cấp cho ông Phạm Văn Th và bà Vũ Thị H;
16. - Yêu cầu định giá lại tài sản tranh chấp vì thời gian định giá đã quá 6 tháng;
17. Bị đơn là bà Vũ Thị H trình bày: Năm 1999 cụ Phạm Văn L là bố chồng bà và là bố đẻ của ông Phạm Văn Th có mua một mảnh đất bao gồm nhà, ao, vườn và 03 sào đất canh tác của cụ Phạm Thị M là mẹ đẻ ông T và bà Trịnh Thị T V là vợ ông T với số tiền là 28.000.000 đồng. Cụ M có làm thủ tục giấy tờ mua bán viết tay cho cụ L, cụ Phạm Văn L giao tiền tại nhà ông Trần Văn Th (nguyên là trưởng khu dân cư Đồng Tử 2) có sự chứng kiến của bà Trịnh Thị T V, bà Phạm Thị B và ông Th. Số tiền  đó  bà  bà  Trịnh  …
18. Ngày 15/3/2002, vợ chồng bà đã được UBND quận K cấp Giấy chứng nhận quyền sử dụng đất (sau đây viết tắt là GCNQSDĐ) số S: 801530 với diện tích 910 m2, mục đích sử dụng “2 lúa”, thời hạn sử dụng đến năm 2020 tại thửa đất trên mà cụ L đã nhận chuyển nhượng của cụ M, bà V.
19. Ngày 03/8/2004, cụ L tiếp tục xác lập đơn đề nghị về việc xin xác nhận thị thực hành chính trong lĩnh vực giao dịch dân sự về nhà ở, đất ở có xác nhận của UBND phường P, K chuyển quyền sử dụng toàn bộ nhà và diện tích đất thổ cư 1.303 m2 tại thửa đất mà cụ L đã nhận chuyển nhượng của cụ M và bà V.
20. Ngày 04/8/2004, UBND phường P, quận K đã lập trích đo thửa đất dùng cho việc đăng ký kê khai sử dụng đất thửa đất số 128, tờ bản đồ số 3000591 -7-(15), tại tổ 4 khu dân cư Đồng Tử 2, phường P, quận K, thành phố Hải Phòng với diện tích 1.303 m2 mang tên vợ chồng bà là Phạm Văn Th và Vũ Thị H.
21. Mọi thủ tục giấy tờ mua bán, hồ sơ cấp giấy chứng nhận quyền sử dụng đất vợ chồng bà và cụ L đã chuyển cho UBND phường P, do cụ Phạm Văn L đã chết nên mọi giấy tờ mua bán giữa cụ M và cụ L vợ chồng bà không tìm thấy.
22. Việc mua bán giữa cụ M và cụ L, ông T và bà V đều biết và không có ý kiến gì. Cụ L đã nhận nhà, đất sử dụng và đã xây dựng nhà xưởng sản xuất, xây tường bao, bờ rào sử dụng trong suốt thời gian từ năm 2001 đến năm 2011 ông T mới có đơn đề nghị UBND phường P giải quyết. Bà H cho rằng việc mua bán nhà, đất giữa cụ L và cụ M là hợp pháp và vợ chồng bà sử dụng từ năm 2001 đến nay không có việc chiếm giữ bất hợp pháp như ông Nguyễn Văn T khai. Vợ chồng bà không đồng ý trả lại nhà và đất ở, đất canh …
23. Tài liệu, chứng cứ để chứng minh cho yêu cầu của mình, bà H nộp cho Tòa án gồm:  Giấy  chứng  nhận  quyền  sử  dụng  đất  số  S:  801530;  Biên  bản  xác  định  ranh giới, mốc giới thửa đất, Trích đo thửa đất để đăng ký kê khai sử dụng đất của UBND phường P cấp cho ông Th, bà H; Đơn đề nghị xin xác nhận giao dịch dân sự về nhà ở,  đất  ở  của  cụ  L  chuyển  quyền  cho  ông  Th,  bà  H;  các  Hợp  đồng,  giấy  tờ  nhận chuyển nhượng QSDĐ của gia đình cụ L với bà Trần Thị Nhinh, bà Trần Thị …
24. Đại diện Ngân hàng NN&PTNT Chi nhánh K (nay là Ngân hàng NN&PTNT Việt  Nam,  Chi  nhánh  quận  K  Đông  Hải  Phòng)  trình  bày:  Tháng  3/1992  ông Nguyễn Văn T có thế chấp tài sản là 01 nhà ở 02 tầng đất 90 m2 và 02 mẫu đầm hồ tại thửa số 905, tờ bản đồ số 01 thuộc xứ Đồng Tử, chỉ giới giáp thửa 933+934, phía Tây  giáp  thửa  988,  phía  Bắc  giáp  thửa  931,  phía  Đông giáp  thửa  902  để đảm  bảo cho hai khoản vay 9.500.000 đồng và EC 26.000.000 đồng, có xác nhận của UBND xã Bắc Hà (BL 19).
25. Năm  2012,  ông  T  đã  thanh  toán  10.000.000  đồng  đối  với  khoản  vay 9.500.000 đồng (trong đó tiền gốc là 9.450.000 đồng, tiền lãi là 550.000 đồng). Đối với khoản vay EC đến nay đã được xóa nợ.   Tính đến ngày 11/5/2021, khoản vay của ông T còn nợ tiền gốc là 50.000.000 đồng, tiền lãi là 9.888.000 đồng, cộng bằng 9.938.000  đồng.  Đại  diện  Ngân  hàng  yêu  cầu  ai  là  người  được  sở  hữu  tài  sản  thế chấp thì phải trả số tiền nêu trên.
26. Tại phiên hòa giải ngày 12 tháng 3 năm 2021 bà V và chị Mai A tự nguyện trả nợ Ngân hàng số tiền nêu trên. Tại phiên tòa bà  V khai tiền nợ Ngân hàng là của gia đình bà, nhưng tài sản thế chấp chưa biết ai được sở hữu cho nên bà chưa có ý kiến về việc này.
27. Người kế thừa quyền nghĩa vụ của nguyên đơn là chị Nguyễn Thị Lan trình bày: Chị là con riêng của ông T, nhưng từ nhỏ chị và ông T không có trách nhiệm gì với nhau, nay chị từ chối tham gia tố tụng. Bà V, chị Mai A, anh Tuấn cũng cho rằng chị Lan không liên quan gì đến vụ việc.
28. Người kế thừa quyền nghĩa vụ của bị đơn bà Phạm Thị T và ông Phạm Văn V, chị Nguyễn Thị L trình bày thống nhất với nhau như sau:
29. Khi  cụ  Phạm  Văn  L  còn  sống,  đã  mua  nhà,  đất  của  cụ  Phạm  Thị  M,  Hợp đồng  chuyển  nhượng  quyền  sở  hữu  nhà  và  sử  dụng  đất  được  viết  giấy  có  người làm chứng.  Cụ  M  đã  nhận  đủ  tiền,  cụ  L  đã  nhận  nhà, đất  và  sử  dụng  ổn  định  từ năm 2001 đến năm 2002 thì cụ L viết giấy chuyển nhượng quyền sử dụng đất nông nghiệp là 910 m2 cho vợ chồng ông Phạm Văn Th và bà Vũ Thị H. Ông Th, bà H đã  được  UBND  quận  K  cấp  giấy  chứng nhận  quyền  sử  dụng (GCNQSD)  đất  …
30. Lời khai của người làm chứng:
31. Ông Trần Văn Th trình bày: Năm 1999-2000, ông là Trưởng khu dân cư Đồng Tử 2 phường P, quận K. Ông được biết cụ M có ý định bán nhà, đất từ rất lâu, sau đó có cụ L đến mua. Hai bên đã thống nhất ra chính quyền làm thủ tục chuyển nhượng, cùng thời điểm đó cụ M có chia đất cho ông C và ông T, mục đích cụ M chia đất cho ông C là để cụ M và bà V bán phần nhà, đất của ông T. Cụ M và bà V vợ ông T đã bán phần đất của ông T cho cụ L với giá khoảng 29 triệu hay 39 triệu ông không nhớ cụ thể, trên đất …
32. Bà Phạm Thị B trình bày: Nguồn gốc đất ông T đang tranh chấp bà không biết của ai, chỉ thấy cụ M bảo bà ra chứng kiến việc trả tiền giữa cụ L và cụ M cùng với bà V (vợ ông T), tại nhà ông Th (cụm trưởng lúc đó) là tiền bán nhà và đất. Cụ L giao cho cụ M 28 triệu đồng, cụ M đưa cho bà V 20 triệu đồng, còn 8 triệu đồng cụ M để lại mua vàng. Bà V (vợ ông T) cùng với bà V (vợ ông Th) lai nhau đi gửi tiền cho ông T, lúc ở nhà bà nghe cụ M nói gửi tiền vào miền Nam cho ông T. Việc bán nhà và đất chủ …
33. Ông Trần Huy C trình bày: Nguồn gốc đất của ông T là do bố mẹ để lại đất thổ cư, tại hồ sơ của UBND phường quản lý có tên của cụ Phạm Thị M, không có tên ông T. Ông T chỉ có hợp đồng thuê đất đầm 5% ở gần nhà ông. Sau khi ông T đi khỏi địa phương UBND phường P đã thu hồi và hủy Hợp đồng thuê đất và ký hợp đồng cho người khác sử dụng, đất 5% này là đất công ích của địa phương… Trong bản xác định ranh  giới  ngày  01/10/1999  là  do  gia  đình  cụ  M  lập  ông  chỉ  chứng  kiến,  sau  đó  gia …
34. Các lời trình bày của ông Nguyễn Anh Văn, Nguyễn Văn Th, Trần Văn Cửu, Lê Sơn Hải, bà Nguyễn Thị Phiên (BL 182 đến 187), bà Nguyễn Thị Loan (BL 189) đều khẳng định nguồn gốc nhà và đất của ông T là của bố mẹ để lại và chỉ nghe kể lại là cụ M và bà V có bán nhà cho cụ L. Lời khai của ông Nguyễn Văn Hễ thì trong thời gian chưa bán nhà, bà V vợ ông T hàng ngày thúc dục cụ M bán nhà để gửi tiền cho ông T. Sau khi bán nhà xong cụ M vào miền Nam một thời gian rồi về thì ở nhà ông Hễ (cạnh nhà cụ M đã …
35. Ý kiến của người bảo vệ quyền và lợi ích hợp pháp của nguyên đơn:
36. Các đương sự và người làm chứng đều xác định  cụ M đã giao dịch chuyển nhượng quyền sử dụng đất và tài sản gắn liền với đất cho cụ L. Bà V đã gửi tiền cho ông T ở thành phố Hồ Chí Minh là có thật. Tuy nhiên, năm 1999 cụ M đã chia đất cho hai người con là ông C và ông T, ông T được sử dụng phần đất có nhà và các công trình phụ do ông T và bà V xây dựng là tài sản của ông T và bà V. Bà V không thể hiện ý chí bán nhà cho cụ L. Việc ông T điện đàm về nhà ông Hài nhờ ông Th bán nhà là có thật, xong …
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 129. Giao dịch dân sự vô hiệu do không tuân thủ quy định về hình thức. Giao dịch dân sự vi phạm quy định điều kiện có hiệu lực về hình thức thì vô hiệu, trừ trường hợp sau đây: 1. Giao dịch dân sự đã được xác lập theo quy định phải bằng văn bản nhưng văn bản không đúng quy định của luật mà một bên hoặc các bên đã thực hiện ít nhất hai phần ba nghĩa vụ trong giao dịch thì theo yêu cầu của một bên hoặc các bên, Tòa án ra quyết định công nhận hiệu lực của giao dịch đó; 2. Giao dịch dân sự đã được xác lập bằng văn bản nhưng vi phạm quy định bắt buộc về công chứng, chứng thực mà một bên hoặc các bên đã thực hiện ít nhất hai phần ba nghĩa vụ trong giao dịch thì theo yêu cầu của một bên hoặc các bên, Tò
3. [BLDS 2015] Điều 73. Huỷ bỏ quyết định tuyên bố chết. 1. Khi một người bị tuyên bố là đã chết trở về hoặc có tin tức xác thực là người đó còn sống thì theo yêu cầu của người đó hoặc của người có quyền, lợi ích liên quan, Tòa án ra quyết định huỷ bỏ quyết định tuyên bố người đó là đã chết. 2. Quan hệ nhân thân của người bị tuyên bố là đã chết được khôi phục khi Tòa án ra quyết định hủy bỏ quyết định tuyên bố người đó là đã chết, trừ trường hợp sau đây: a) Vợ hoặc chồng của người bị tuyên bố là đã chết đã được Tòa án cho ly hôn theo quy định tại khoản 2 Điều 68 của Bộ luật này thì quyết định cho ly hôn vẫn có hiệu lực pháp luật; b) Vợ hoặc chồng của người bị tuyên bố là đã chết đã kết hôn với người khác thì việc k
4. [BLDS 2015] Điều 531. Hình thức hợp đồng vận chuyển tài sản. 1. Hợp đồng vận chuyển tài sản được giao kết bằng văn bản, bằng lời nói hoặc được xác lập bằng hành vi cụ thể. 2. Vận đơn hoặc chứng từ vận chuyển tương đương khác là bằng chứng của việc giao kết hợp đồng giữa các bên
5. [BLDS 2015] Điều 51. Giám sát việc giám hộ. 1. Người thân thích của người được giám hộ thỏa thuận cử người giám sát việc giám hộ trong số những người thân thích hoặc chọn cá nhân, pháp nhân khác làm người giám sát việc giám hộ. Việc cử, chọn người giám sát việc giám hộ phải được sự đồng ý của người đó. Trường hợp giám sát việc giám hộ liên quan đến quản lý tài sản của người được giám hộ thì người giám sát phải đăng ký tại Ủy ban nhân dân cấp xã nơi cư trú của người được giám hộ. Người thân thích của người được giám hộ là vợ, chồng, cha, mẹ, con của người được giám hộ; nếu không có ai trong số những người này thì người thân thích của người được giám hộ là ông, bà, anh ruột, chị ruột, em ruột của người được giám h
Please suggest hypotheses to support why the outcome of the case might be the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hoàn toàn hay một phần, chúng ta cần phân tích từng yếu tố trong vụ kiện:

1. **Quyền sở hữu đất**: 
   - Theo đơn khởi kiện, ông Nguyễn Văn T được mẹ đẻ là cụ Phạm Thị M chia đất. 
   - Tuy nhiên, ông T đã thế chấp đất cho Ngân hàng N vào năm 1992 và 1997, và sau đó bị mất khả năng thanh toán nợ.
   - Việc ông T thế chấp đất cho Ngân hàng N không có sự đồng ý của gia đình cụ Phạm Thị M, gây ra tranh chấp.

2. **Thỏa thuận chuyển nhượng quyền sử dụng đất**:
   - Theo lời khai của bà Trịnh Thị T V, gia đình cụ Phạm Văn L và bà Vũ Thị H đã mua bán nhà, đất từ cụ Phạm Thị M vào năm 1999.
   - Tuy nhiên, không có giấy tờ chính thức ghi nhận giao dịch này, chỉ có các tài liệu viết tay và chứng kiến.

3. **Hợp đồng thế chấp và quyền sở hữu tài sản**:
   - Ông T đã thế chấp tài sản cho Ngân hàng N vào năm 1992, nhưng không có giao dịch chuyển nhượng quyền sử dụng đất hợp pháp.
   - Việc ông T thế chấp tài sản mà không có sự đồng ý của gia đình cụ Phạm Thị M là vi phạm pháp luật.

4. **Giấy chứng nhận quyền sử dụng đất**:
   - Bà Vũ Thị H đã được UBND quận K cấp giấy chứng nhận quyền sử dụng đất (GCNQSDĐ) số S: 801530 vào năm 2002.
   - Tuy nhiên, giấy chứng nhận này không có cơ sở pháp lý hợp lệ.

5. **Thành phần tố tụng và quyền lợi liên quan**:
   - Người kế thừa quyền và nghĩa vụ của nguyên đơn là bà Trịnh Thị T V.
   - Người kế thừa quyền và nghĩa vụ của bị đơn là bà Phạm Thị T và ông Phạm Văn V.
   - Người làm chứng và đại diện Ngân hàng N đều xác nhận rằng giao dịch giữa cụ Phạm Văn L và cụ Phạm Thị M là hợp pháp.

Từ phân tích trên, có thể đưa ra một số giả thuyết hỗ trợ cho việc Tòa án có thể chấp nhận yêu cầu của nguyên đơn:

- **Yêu cầu tuyên bố hợp đồng mua bán vô hiệu**: 
  - Nếu Tòa án xác định rằng giao dịch giữa cụ Phạm Văn L và cụ Phạm Thị M không tuân thủ quy định về hình thức, thì có thể tuyên bố hợp đồng mua bán vô hiệu.
  
- **Yêu cầu trả lại diện tích nhà và đất**: 
  - Nếu Tòa án xác định
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge rejected all
```

## Result
- outcome: **the court rejects all of the plaintiff's claims**
- converged: True
- accepted hypotheses: