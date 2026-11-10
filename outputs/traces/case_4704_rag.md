# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Theo đơn khởi kiện ngày 01/07/2013 và trong quá trình tố tụng, nguyên đơn ông Lê Phú L và đại diện hợp pháp theo ủy quyền của nguyên đơn là bà Đỗ Lê Tuyết P trình bày:
2. Nguồn gốc nhà và đất tọa lạc tại số MC, Phường 15, Quận 8, Thành phố Hồ Chí Minh (nhà MC) là của ông Lê Văn S (chết năm 1984) và bà Ngô Thị N (chết năm 2005). Ông S và bà N có tất cả 04 người con:
3. 1/ Bà Lê Thị Đ, sinh năm 1953.
4. 2/ Ông Lê Phú T, sinh năm 1954.
5. 3/ Bà Lê Kim T, sinh năm 1955.
6. 4/ Ông Lê Phú L, sinh năm 1957.
7. Cha mẹ ông S, bà N đã chết trước, ngoài 04 người con như trên thì ông S, bà N không có con riêng hoặc con nuôi. Khi chết ông S và bà N không để lại di chúc.
8. Di sản để lại gồm có nhà đất tọa lạc tại số MC và các vật dụng sinh hoạt trong nhà gồm: 01 tủ thờ gỗ cẩn xà, 01 bộ bàn ghế tiếp khách (01 bàn và 06 cái ghế), 01 bộ bàn ghế (salon) gỗ cẩm lai. Vào năm 2000, bà Lê Kim T đã chi số tiền 10.000 USD, tương đương 200.000.000 đồng để sửa chữa lại toàn bộ căn nhà. Ngoài những tài sản trên, không còn di sản nào của ông S, bà N để lại.
9. Căn nhà trước đây do ông S, bà N đứng tên. Hiện nay, căn nhà đang do ông Lê Phú L và bà Lê Thị Đ cùng quản lý và sử dụng. Ông Lê Phú T đã có gia đình và ra ở riêng từ rất lâu tại địa chỉ RC, Phường 15, Quận 8, Thành phố Hồ Chí Minh; bà Lê Kim T thì đang sinh sống tại Mỹ. Ông L, bà Đ và bà T đã thỏa thuận tài sản chung của ông S để lại và di sản thừa kế của bà N sẽ chia đều cho 04 người, mỗi người một phần bằng nhau, nhưng ông Lê Phú T không đồng ý và yêu cầu chỉ chia cho 02 người con trai là …
10. Nay nguyên đơn yêu cầu: Sau khi trừ đi số tiền 200.000.000 đồng của bà T chi ra để sửa chữa toàn bộ căn nhà, phần giá trị tài sản trên còn bao nhiêu thì chia đều cho 04 chị em là bà Đ, ông T, bà T, ông L. Ông L xin giữ lại căn nhà và các tài sản, vật dụng có trong căn nhà để thờ cúng, hương hỏa và xin trả giá trị phần thừa kế cho các đồng thừa kế.
11. Đối với yêu cầu phản tố của bị đơn, nguyên đơn trình bày: Căn nhà số HSK, Phường 14, Quận 8, Thành phố Hồ Chí Minh (nhà HSK) không phải là di sản của ông S, bà N để lại mà là tài sản riêng của bà Lê Thị Đ. Nguyên đơn không đồng ý với yêu cầu phản tố của bị đơn về việc chia căn nhà HSK cho nguyên đơn và các đồng thừa kế khác.
12. Đối với các vật dụng khác theo lời khai của bị đơn đều do ông L và bà Đ mua gồm: 01 bộ ván gỗ dày gồm 03 tấm, 01 bộ ván gỗ mỏng gồm 02 tấm, 01 tủ đựng quần áo dài gỗ cẩm lai và 01 tủ đựng quần áo gỗ đen.
13. Chi phí đo vẽ, định giá trước đây do nguyên đơn tạm ứng nay yêu cầu các bên cùng chịu theo tỷ lệ được hưởng di sản.
14. Tại phiên tòa, nguyên đơn xác định nguyên đơn không yêu cầu Tòa án xem xét giải quyết đối với công sức quản lý di sản của nguyên đơn.
15. Bị đơn ông Lê Phú T có đại diện hợp pháp theo ủy quyền là ông Phạm Trung Đ và bà Phạm Thị Ngọc T trình bày:
16. Thống nhất trình bày của nguyên đơn về nguồn gốc nhà và đất. Bị đơn cũng xác nhận hàng thừa kế của ông S, bà N đúng như nguyên đơn trình bày.
17. Lúc còn sống ông S đã nêu ý nguyện là khi chết sẽ để lại căn nhà MC cho hai người con trai là ông L và ông T, còn hai người con gái là bà Đ và bà T thì đã theo chồng ra ở riêng. Trong quá trình sinh sống, bị đơn đã bỏ tiền ra sửa chữa một phần nhà vào khoảng trước năm 1980, tuy nhiên ông T không có yêu cầu đối với phần sửa chữa này vì chỉ là sửa chữa nhỏ.
18. Nay ông L khởi kiện yêu cầu chia thừa kế căn nhà MC, bị đơn xác định di sản của ông Lê Văn S và bà Ngô Thị N ngoài căn nhà MC, còn có căn nhà HSK. Ngoài các vật dụng trong nhà mà bị đơn đã thống nhất, như nguyên đơn trình bày, thì di sản còn những vật dụng như sau: 01 bộ ván gỗ dày gồm 03 tấm, 01 bộ ván gỗ mỏng gồm 02 tấm, 01 tủ đựng quần áo dài gỗ cẩm lai, 01 tủ đựng quần áo gỗ đen. Những đồ vật này do nguyên đơn quản lý tại nhà MC.
19. Bị đơn đồng ý với số tiền 200.000.000 đồng chi phí sửa chữa nhà MC của bà T nếu có hóa đơn, chứng từ chứng minh. Sau khi trừ số tiền 200.000.000 đồng này trả cho bà Lê Kim T, số tiền còn lại của 02 căn nhà nói trên chia cho 04 người thừa kế của ông S và bà N. Bị đơn muốn được nhận di sản bằng hiện vật và sẽ hoàn lại giá trị cho các đồng thừa kế. Bị đơn yêu cầu được nhận phần nhà đất MC, phần có vị trí nhìn từ ngoài đường vào phía bên tay phải. Lý do ông T là con trai trưởng và không có nhà nào …
20. Ngày 20 tháng 4 năm 2016 bị đơn ông Lê Phú T có “Đơn yêu cầu phản tố” với nội dung:
21. Căn nhà HSK có nguồn gốc do bác ruột là ông Lê Văn T tạo lập. Sau giải phóng, ông T cùng gia đình vượt biên. Trước khi đi, ông T đã cho cha của ông (ông S) căn nhà trên. Việc cho nhận căn nhà HSK giữa ông T và ông S được ông S nói cho các con trong nhà biết. Cha mẹ ông quản lý và sử dụng căn nhà nêu trên một thời gian. Ý nguyện của cha mẹ ông là căn nhà MC là căn nhà đôi nên sẽ ngăn làm hai cho ông L và ông. Căn nhà HSK mà bác T cho sẽ cho chị ông là bà Đ. Vì vậy, sau này cha mẹ ông đã giao cho …
22. Toàn bộ hồ sơ bà Lê Thị Đ xin cấp giấy chứng nhận quyền sử dụng đất và quyền sở hữu nhà ở số HSK là khai trình gian dối. Ông yêu cầu Tòa án xác định căn nhà HSK là di sản của ông Lê Văn S và bà Ngô Thị N, ông yêu cầu được nhận ¼ giá trị, ước tính phần này là 750.000.000 đồng.
23. Bị đơn yêu cầu hủy giấy chứng nhận số BG 971829, số vào sổ CH00739 do Ủy ban nhân dân Quận 8 cấp ngày 14/02/2012 cho bà Lê Thị Đ.
24. Tại phiên tòa, bị đơn xác định nếu bị đơn được nhận hiện vật là ½ nhà MC thì bị đơn tự nguyện hỗ trợ cho bà T số tiền 100.000.000 đồng vì bà T có công sửa chữa nhà.
25. Những người có quyền lợi, nghĩa vụ liên quan: bà Lê Thị Đ và bà Lê Kim T có người đại diện theo ủy quyền là bà Nguyễn Thị Ngọc H trình bày:
26. Thống nhất với lời trình bày và đồng ý với yêu cầu của nguyên đơn về di sản thừa kế và hàng thừa kế.
27. Tại “Bản tự khai” ngày 20/3/2017, đại diện của bà T là bà Nguyễn Thị Ngọc H trình bày: Đối với số tiền 200.000.000 đồng trước đây bà Thuận bỏ ra sửa chữa nhà MC, bà không lưu lại các chứng từ hóa đơn sửa chữa, vì thời điểm đó mẹ của bà T (cụ N) còn sống nên bà T muốn sửa nhà cho mẹ ở. Bà T không có yêu cầu đối với số tiền 200.000.000 đồng đã bỏ ra sửa nhà.
28. Đối với yêu cầu phản tố của bị đơn, đại diện theo ủy quyền của bà Đ và bà xác định căn nhà HSK, Phường 14, Quận 8 là tài sản riêng của bà Đ, không phải di sản của ông S và bà N.
29. Tại phiên tòa, đại diện của bà Đ xác định bà Đ không yêu cầu Tòa án xem xét giải quyết đối với công sức quản lý di sản của bà Đ. Đại diện của bà T xác định bà T không yêu cầu Tòa án xem xét giải quyết đối với chi phí sửa chữa nhà MC, nhưng nếu các đồng thừa kế hỗ trợ phần chi phí sửa chữa này thì bà T đồng ý nhận.
30. Người có quyền lợi, nghĩa vụ liên quan ông Lê Phú K trình bày:
31. Thống nhất với ý kiến của bị đơn và xin vắng mặt trong suốt quá trình giải quyết vụ án.
32. Người có quyền lợi, nghĩa vụ liên quan là Ủy ban nhân dân Quận 8, Thành phố Hồ Chí Minh có đại diện hợp pháp theo ủy quyền là ông Hồ Thanh B trình bày:
33. Căn nhà số HSK, Phường 14, Quận 8, Thành phố Hồ Chí Minh (số cũ là 33 HSK) có nguồn gốc của ông Lê Văn T cho bà Lê Thị Đ bằng giấy tay ngày 22/8/1975. Đến năm 1999, bà Đ kê khai đăng ký nhà đất, ngày 02/11/2011 bà Đ có đơn đề nghị cấp giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất. Ủy ban nhân dân Quận 8 đã cấp Giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất số BG 971829, số vào sổ cấp giấy chứng nhận CH00739 ngày …
34. Tại phiên tòa, các đương sự đã tự thỏa thuận và yêu cầu Tòa án ghi nhận trong bản án những vấn đề đã thỏa thuận như sau:
35. Giao cho ông Lê Phú L được hưởng những di sản sau: 01 bộ bàn ghế (01 bàn và 06 cái ghế), 01 bộ bàn ghế (salon) gỗ cẩm lai, 01 bộ ván gỗ 03 tấm, 01 bộ ván gỗ 02 tấm, 01 tủ đựng quần áo gỗ cẩm lai, 01 tủ đựng quần áo gỗ đen. Những tài sản này do ông L đang quản lý. Giao cho ông Lê Phú T được hưởng di sản là 01 tủ thờ gỗ cẩn xà cừ do ông L đang quản lý có trách nhiệm giao cho ông T.
36. Chi phí định giá 2.000.000 đồng nguyên đơn đã nộp, nay ông T, bà Đ, bà T mỗi người trả lại cho ông L là 500.000 đồng.
37. Về thời hiệu khởi kiện về thừa kế: Thời điểm Tòa án thụ lý đơn khởi kiện của nguyên đơn là ngày 01/10/2013. Vụ án có đương sự ở nước ngoài, bị đơn và tài sản tranh chấp tại Thành phố Hồ Chí Minh. Đương sự vắng mặt có đơn yêu cầu giải quyết vắng mặt.  Thời điểm phát sinh tranh chấp theo Đơn khởi kiện ngày 01/10/2013.
38. Cụ Lê Văn S chết năm 1984 và cụ Ngô Thị N chết năm 2005, cha mẹ của cụ S và cụ N đều đã chết trước hai cụ. Hàng thừa kế thứ nhất của cụ S và cụ N gồm:
39. - Bà Lê Thị Đ, sinh năm 1953;
40. - Ông Lê Phú T, sinh năm 1954;
41. - Bà Lê Kim T, sinh năm 1955;
42. - Ông Lê Phú L, sinh năm 1957.
43. Các đương sự thống nhất thừa nhận về người thừa kế nêu trên.
44. Nhà ở, đất ở tại số MC theo Bản kê khai nhà cửa ngày 22/12/1977 có xác nhận của Ủy ban nhân dân, có giá trị là 3.230.934.000 đồng.
45. Các vật dụng gồm:
46. - 01 tủ thờ gỗ cẩn xà cừ;
47. - 01 bộ bàn ghế tiếp khách (01 bàn và 06 cái ghế);
48. - 01 bộ bàn ghế (salon) gỗ cẩm lai.
49. Các tài sản này hiện nay do nguyên đơn đang quản lý.
50. Các đương sự đều thống nhất các tài sản trên là di sản của cụ S và cụ N, thống nhất về giá trị của tài sản, đồng thời xác định cụ S và cụ N không để lại di chúc.
51. Theo văn bản trả lời số 234/VPĐK-LT&CNTT ngày 17/9/2014 của Văn phòng đăng ký quyền sử dụng đất Quận 8 kèm theo bản sao hồ sơ lưu trữ cung cấp thể hiện:
52. Nguồn gốc nhà đất HSK do ông La Nghĩa bán cho ông Lê Văn Thịnh từ năm 1968. Năm 1975, ông Lê Văn Thịnh tặng cho bà Lê Thị Đ theo giấy tay ghi ngày 22/8/1975. Bà Lê Thị Đ đã được cấp giấy chứng nhận quyền sở hữu nhà ở và quyền sử dụng đất số BG 971829, số vào sổ CH00739 ngày 14/02/2012. Bị đơn không có tài liệu chứng cứ nào để chứng minh nhà đất này là di sản của cụ S và cụ N.
53. Theo “Bản tự khai” ngày 20/3/2017, đại diện của bà Lê Kim T trình bày: Đối với số tiền 200.000.000 đồng trước đây bà Lê Kim T bỏ ra sửa chữa nhà MC vào năm 2000, bà Lê Kim T không lưu lại các chứng từ hóa đơn sửa chữa, vì thời điểm đó mẹ của bà Lê Kim T (cụ N) còn sống nên bà Lê Kim T muốn sửa nhà cho mẹ ở. Các đương sự thừa nhận có sự việc sửa nhà.
54. Nhà MC do ông Lê Phú L và bà Lê Thị Đ quản lý. Nguyên đơn và đại diện của bà Lê Thị Đ tại phiên tòa đều xác định không yêu cầu Tòa án giải quyết về công sức quản lý đối với di sản.
55. Phần đất tại MC có diện tích 210,2m2, chiều ngang mặt tiền 6,78m. Nguồn gốc nhà MC trước đó là từ hai căn nhà ghép lại.
56. Bà Lê Kim T đang định cư ở nước ngoài.
57. Bà Lê Thị Đ đã có chỗ ở là nhà HSK, Phường 14, Quận 8.
58. Ông Lê Phú L và ông Lê Phú T hiện nay chưa sở hữu một căn nhà nào khác.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
3. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
4. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
5. [BLDS 2015] Điều 656. Họp mặt những người thừa kế. 1. Sau khi có thông báo về việc mở thừa kế hoặc di chúc được công bố, những người thừa kế có thể họp mặt để thoả thuận những việc sau đây: a) Cử người quản lý di sản, người phân chia di sản, xác định quyền, nghĩa vụ của những người này, nếu người để lại di sản không chỉ định trong di chúc; b) Cách thức phân chia di sản. 2. Mọi thoả thuận của những người thừa kế phải được lập thành văn bản
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá yêu cầu của nguyên đơn, chúng ta cần phân tích từng phần yêu cầu:

1. Yêu cầu chia tài sản: 
- Theo quy định tại Điều 656 BLDS 2015, nguyên đơn yêu cầu chia tài sản bằng hiện vật. Tuy nhiên, tài sản cụ thể (nhà và các vật dụng) hiện đang do ông Lê Phú L và bà Lê Thị Đ quản lý và sử dụng.
- Theo Điều 660 BLDS 2015, khi phân chia di sản theo pháp luật, nếu không thể chia bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật. 

2. Yêu cầu giữ lại nhà và các tài sản:
- Ông Lê Phú L yêu cầu giữ lại căn nhà và các tài sản, vật dụng có trong căn nhà để thờ cúng, hương hỏa. Điều này không vi phạm pháp luật.

3. Yêu cầu trả giá trị phần thừa kế:
- Ông Lê Phú L xin trả giá trị phần thừa kế cho các đồng thừa kế. Điều này không vi phạm pháp luật.

4. Yêu cầu chia tài sản theo tỷ lệ:
- Theo yêu cầu của ông Lê Phú L, tài sản chia đều cho 04 người thừa kế là bà Đ, ông T, bà T, ông L. Điều này tuân thủ pháp luật.

5. Yêu cầu chia tài sản theo hiện vật:
- Ông Lê Phú L yêu cầu chia tài sản theo hiện vật. Điều này cũng tuân thủ pháp luật.

6. Yêu cầu chia tài sản theo tỷ lệ:
- Ông Lê Phú L yêu cầu chia tài sản theo tỷ lệ. Điều này cũng tuân thủ pháp luật.

7. Yêu cầu chia tài sản theo hiện vật:
- Ông Lê Phú L yêu cầu chia tài sản theo hiện vật. Điều này cũng tuân thủ pháp luật.

Như vậy, tất cả các yêu cầu của ông Lê Phú L đều tuân thủ pháp luật và không vi phạm quyền lợi của các đương sự khác.

Kết luận: Yêu cầu của nguyên đơn được chấp nhận (tất cả).

YESSAOÝ MEGINHANCHECK NGAY
```

## A.2#1 — abductive (defendant)

**Prompt**
```
Considering the following facts:
1. Theo đơn khởi kiện ngày 01/07/2013 và trong quá trình tố tụng, nguyên đơn ông Lê Phú L và đại diện hợp pháp theo ủy quyền của nguyên đơn là bà Đỗ Lê Tuyết P trình bày:
2. Nguồn gốc nhà và đất tọa lạc tại số MC, Phường 15, Quận 8, Thành phố Hồ Chí Minh (nhà MC) là của ông Lê Văn S (chết năm 1984) và bà Ngô Thị N (chết năm 2005). Ông S và bà N có tất cả 04 người con:
3. 1/ Bà Lê Thị Đ, sinh năm 1953.
4. 2/ Ông Lê Phú T, sinh năm 1954.
5. 3/ Bà Lê Kim T, sinh năm 1955.
6. 4/ Ông Lê Phú L, sinh năm 1957.
7. Cha mẹ ông S, bà N đã chết trước, ngoài 04 người con như trên thì ông S, bà N không có con riêng hoặc con nuôi. Khi chết ông S và bà N không để lại di chúc.
8. Di sản để lại gồm có nhà đất tọa lạc tại số MC và các vật dụng sinh hoạt trong nhà gồm: 01 tủ thờ gỗ cẩn xà, 01 bộ bàn ghế tiếp khách (01 bàn và 06 cái ghế), 01 bộ bàn ghế (salon) gỗ cẩm lai. Vào năm 2000, bà Lê Kim T đã chi số tiền 10.000 USD, tương đương 200.000.000 đồng để sửa chữa lại toàn bộ căn nhà. Ngoài những tài sản trên, không còn di sản nào của ông S, bà N để lại.
9. Căn nhà trước đây do ông S, bà N đứng tên. Hiện nay, căn nhà đang do ông Lê Phú L và bà Lê Thị Đ cùng quản lý và sử dụng. Ông Lê Phú T đã có gia đình và ra ở riêng từ rất lâu tại địa chỉ RC, Phường 15, Quận 8, Thành phố Hồ Chí Minh; bà Lê Kim T thì đang sinh sống tại Mỹ. Ông L, bà Đ và bà T đã thỏa thuận tài sản chung của ông S để lại và di sản thừa kế của bà N sẽ chia đều cho 04 người, mỗi người một phần bằng nhau, nhưng ông Lê Phú T không đồng ý và yêu cầu chỉ chia cho 02 người con trai là …
10. Nay nguyên đơn yêu cầu: Sau khi trừ đi số tiền 200.000.000 đồng của bà T chi ra để sửa chữa toàn bộ căn nhà, phần giá trị tài sản trên còn bao nhiêu thì chia đều cho 04 chị em là bà Đ, ông T, bà T, ông L. Ông L xin giữ lại căn nhà và các tài sản, vật dụng có trong căn nhà để thờ cúng, hương hỏa và xin trả giá trị phần thừa kế cho các đồng thừa kế.
11. Đối với yêu cầu phản tố của bị đơn, nguyên đơn trình bày: Căn nhà số HSK, Phường 14, Quận 8, Thành phố Hồ Chí Minh (nhà HSK) không phải là di sản của ông S, bà N để lại mà là tài sản riêng của bà Lê Thị Đ. Nguyên đơn không đồng ý với yêu cầu phản tố của bị đơn về việc chia căn nhà HSK cho nguyên đơn và các đồng thừa kế khác.
12. Đối với các vật dụng khác theo lời khai của bị đơn đều do ông L và bà Đ mua gồm: 01 bộ ván gỗ dày gồm 03 tấm, 01 bộ ván gỗ mỏng gồm 02 tấm, 01 tủ đựng quần áo dài gỗ cẩm lai và 01 tủ đựng quần áo gỗ đen.
13. Chi phí đo vẽ, định giá trước đây do nguyên đơn tạm ứng nay yêu cầu các bên cùng chịu theo tỷ lệ được hưởng di sản.
14. Tại phiên tòa, nguyên đơn xác định nguyên đơn không yêu cầu Tòa án xem xét giải quyết đối với công sức quản lý di sản của nguyên đơn.
15. Bị đơn ông Lê Phú T có đại diện hợp pháp theo ủy quyền là ông Phạm Trung Đ và bà Phạm Thị Ngọc T trình bày:
16. Thống nhất trình bày của nguyên đơn về nguồn gốc nhà và đất. Bị đơn cũng xác nhận hàng thừa kế của ông S, bà N đúng như nguyên đơn trình bày.
17. Lúc còn sống ông S đã nêu ý nguyện là khi chết sẽ để lại căn nhà MC cho hai người con trai là ông L và ông T, còn hai người con gái là bà Đ và bà T thì đã theo chồng ra ở riêng. Trong quá trình sinh sống, bị đơn đã bỏ tiền ra sửa chữa một phần nhà vào khoảng trước năm 1980, tuy nhiên ông T không có yêu cầu đối với phần sửa chữa này vì chỉ là sửa chữa nhỏ.
18. Nay ông L khởi kiện yêu cầu chia thừa kế căn nhà MC, bị đơn xác định di sản của ông Lê Văn S và bà Ngô Thị N ngoài căn nhà MC, còn có căn nhà HSK. Ngoài các vật dụng trong nhà mà bị đơn đã thống nhất, như nguyên đơn trình bày, thì di sản còn những vật dụng như sau: 01 bộ ván gỗ dày gồm 03 tấm, 01 bộ ván gỗ mỏng gồm 02 tấm, 01 tủ đựng quần áo dài gỗ cẩm lai, 01 tủ đựng quần áo gỗ đen. Những đồ vật này do nguyên đơn quản lý tại nhà MC.
19. Bị đơn đồng ý với số tiền 200.000.000 đồng chi phí sửa chữa nhà MC của bà T nếu có hóa đơn, chứng từ chứng minh. Sau khi trừ số tiền 200.000.000 đồng này trả cho bà Lê Kim T, số tiền còn lại của 02 căn nhà nói trên chia cho 04 người thừa kế của ông S và bà N. Bị đơn muốn được nhận di sản bằng hiện vật và sẽ hoàn lại giá trị cho các đồng thừa kế. Bị đơn yêu cầu được nhận phần nhà đất MC, phần có vị trí nhìn từ ngoài đường vào phía bên tay phải. Lý do ông T là con trai trưởng và không có nhà nào …
20. Ngày 20 tháng 4 năm 2016 bị đơn ông Lê Phú T có “Đơn yêu cầu phản tố” với nội dung:
21. Căn nhà HSK có nguồn gốc do bác ruột là ông Lê Văn T tạo lập. Sau giải phóng, ông T cùng gia đình vượt biên. Trước khi đi, ông T đã cho cha của ông (ông S) căn nhà trên. Việc cho nhận căn nhà HSK giữa ông T và ông S được ông S nói cho các con trong nhà biết. Cha mẹ ông quản lý và sử dụng căn nhà nêu trên một thời gian. Ý nguyện của cha mẹ ông là căn nhà MC là căn nhà đôi nên sẽ ngăn làm hai cho ông L và ông. Căn nhà HSK mà bác T cho sẽ cho chị ông là bà Đ. Vì vậy, sau này cha mẹ ông đã giao cho …
22. Toàn bộ hồ sơ bà Lê Thị Đ xin cấp giấy chứng nhận quyền sử dụng đất và quyền sở hữu nhà ở số HSK là khai trình gian dối. Ông yêu cầu Tòa án xác định căn nhà HSK là di sản của ông Lê Văn S và bà Ngô Thị N, ông yêu cầu được nhận ¼ giá trị, ước tính phần này là 750.000.000 đồng.
23. Bị đơn yêu cầu hủy giấy chứng nhận số BG 971829, số vào sổ CH00739 do Ủy ban nhân dân Quận 8 cấp ngày 14/02/2012 cho bà Lê Thị Đ.
24. Tại phiên tòa, bị đơn xác định nếu bị đơn được nhận hiện vật là ½ nhà MC thì bị đơn tự nguyện hỗ trợ cho bà T số tiền 100.000.000 đồng vì bà T có công sửa chữa nhà.
25. Những người có quyền lợi, nghĩa vụ liên quan: bà Lê Thị Đ và bà Lê Kim T có người đại diện theo ủy quyền là bà Nguyễn Thị Ngọc H trình bày:
26. Thống nhất với lời trình bày và đồng ý với yêu cầu của nguyên đơn về di sản thừa kế và hàng thừa kế.
27. Tại “Bản tự khai” ngày 20/3/2017, đại diện của bà T là bà Nguyễn Thị Ngọc H trình bày: Đối với số tiền 200.000.000 đồng trước đây bà Thuận bỏ ra sửa chữa nhà MC, bà không lưu lại các chứng từ hóa đơn sửa chữa, vì thời điểm đó mẹ của bà T (cụ N) còn sống nên bà T muốn sửa nhà cho mẹ ở. Bà T không có yêu cầu đối với số tiền 200.000.000 đồng đã bỏ ra sửa nhà.
28. Đối với yêu cầu phản tố của bị đơn, đại diện theo ủy quyền của bà Đ và bà xác định căn nhà HSK, Phường 14, Quận 8 là tài sản riêng của bà Đ, không phải di sản của ông S và bà N.
29. Tại phiên tòa, đại diện của bà Đ xác định bà Đ không yêu cầu Tòa án xem xét giải quyết đối với công sức quản lý di sản của bà Đ. Đại diện của bà T xác định bà T không yêu cầu Tòa án xem xét giải quyết đối với chi phí sửa chữa nhà MC, nhưng nếu các đồng thừa kế hỗ trợ phần chi phí sửa chữa này thì bà T đồng ý nhận.
30. Người có quyền lợi, nghĩa vụ liên quan ông Lê Phú K trình bày:
31. Thống nhất với ý kiến của bị đơn và xin vắng mặt trong suốt quá trình giải quyết vụ án.
32. Người có quyền lợi, nghĩa vụ liên quan là Ủy ban nhân dân Quận 8, Thành phố Hồ Chí Minh có đại diện hợp pháp theo ủy quyền là ông Hồ Thanh B trình bày:
33. Căn nhà số HSK, Phường 14, Quận 8, Thành phố Hồ Chí Minh (số cũ là 33 HSK) có nguồn gốc của ông Lê Văn T cho bà Lê Thị Đ bằng giấy tay ngày 22/8/1975. Đến năm 1999, bà Đ kê khai đăng ký nhà đất, ngày 02/11/2011 bà Đ có đơn đề nghị cấp giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất. Ủy ban nhân dân Quận 8 đã cấp Giấy chứng nhận quyền sử dụng đất, quyền sở hữu nhà ở và tài sản khác gắn liền với đất số BG 971829, số vào sổ cấp giấy chứng nhận CH00739 ngày …
34. Tại phiên tòa, các đương sự đã tự thỏa thuận và yêu cầu Tòa án ghi nhận trong bản án những vấn đề đã thỏa thuận như sau:
35. Giao cho ông Lê Phú L được hưởng những di sản sau: 01 bộ bàn ghế (01 bàn và 06 cái ghế), 01 bộ bàn ghế (salon) gỗ cẩm lai, 01 bộ ván gỗ 03 tấm, 01 bộ ván gỗ 02 tấm, 01 tủ đựng quần áo gỗ cẩm lai, 01 tủ đựng quần áo gỗ đen. Những tài sản này do ông L đang quản lý. Giao cho ông Lê Phú T được hưởng di sản là 01 tủ thờ gỗ cẩn xà cừ do ông L đang quản lý có trách nhiệm giao cho ông T.
36. Chi phí định giá 2.000.000 đồng nguyên đơn đã nộp, nay ông T, bà Đ, bà T mỗi người trả lại cho ông L là 500.000 đồng.
37. Về thời hiệu khởi kiện về thừa kế: Thời điểm Tòa án thụ lý đơn khởi kiện của nguyên đơn là ngày 01/10/2013. Vụ án có đương sự ở nước ngoài, bị đơn và tài sản tranh chấp tại Thành phố Hồ Chí Minh. Đương sự vắng mặt có đơn yêu cầu giải quyết vắng mặt.  Thời điểm phát sinh tranh chấp theo Đơn khởi kiện ngày 01/10/2013.
38. Cụ Lê Văn S chết năm 1984 và cụ Ngô Thị N chết năm 2005, cha mẹ của cụ S và cụ N đều đã chết trước hai cụ. Hàng thừa kế thứ nhất của cụ S và cụ N gồm:
39. - Bà Lê Thị Đ, sinh năm 1953;
40. - Ông Lê Phú T, sinh năm 1954;
41. - Bà Lê Kim T, sinh năm 1955;
42. - Ông Lê Phú L, sinh năm 1957.
43. Các đương sự thống nhất thừa nhận về người thừa kế nêu trên.
44. Nhà ở, đất ở tại số MC theo Bản kê khai nhà cửa ngày 22/12/1977 có xác nhận của Ủy ban nhân dân, có giá trị là 3.230.934.000 đồng.
45. Các vật dụng gồm:
46. - 01 tủ thờ gỗ cẩn xà cừ;
47. - 01 bộ bàn ghế tiếp khách (01 bàn và 06 cái ghế);
48. - 01 bộ bàn ghế (salon) gỗ cẩm lai.
49. Các tài sản này hiện nay do nguyên đơn đang quản lý.
50. Các đương sự đều thống nhất các tài sản trên là di sản của cụ S và cụ N, thống nhất về giá trị của tài sản, đồng thời xác định cụ S và cụ N không để lại di chúc.
51. Theo văn bản trả lời số 234/VPĐK-LT&CNTT ngày 17/9/2014 của Văn phòng đăng ký quyền sử dụng đất Quận 8 kèm theo bản sao hồ sơ lưu trữ cung cấp thể hiện:
52. Nguồn gốc nhà đất HSK do ông La Nghĩa bán cho ông Lê Văn Thịnh từ năm 1968. Năm 1975, ông Lê Văn Thịnh tặng cho bà Lê Thị Đ theo giấy tay ghi ngày 22/8/1975. Bà Lê Thị Đ đã được cấp giấy chứng nhận quyền sở hữu nhà ở và quyền sử dụng đất số BG 971829, số vào sổ CH00739 ngày 14/02/2012. Bị đơn không có tài liệu chứng cứ nào để chứng minh nhà đất này là di sản của cụ S và cụ N.
53. Theo “Bản tự khai” ngày 20/3/2017, đại diện của bà Lê Kim T trình bày: Đối với số tiền 200.000.000 đồng trước đây bà Lê Kim T bỏ ra sửa chữa nhà MC vào năm 2000, bà Lê Kim T không lưu lại các chứng từ hóa đơn sửa chữa, vì thời điểm đó mẹ của bà Lê Kim T (cụ N) còn sống nên bà Lê Kim T muốn sửa nhà cho mẹ ở. Các đương sự thừa nhận có sự việc sửa nhà.
54. Nhà MC do ông Lê Phú L và bà Lê Thị Đ quản lý. Nguyên đơn và đại diện của bà Lê Thị Đ tại phiên tòa đều xác định không yêu cầu Tòa án giải quyết về công sức quản lý đối với di sản.
55. Phần đất tại MC có diện tích 210,2m2, chiều ngang mặt tiền 6,78m. Nguồn gốc nhà MC trước đó là từ hai căn nhà ghép lại.
56. Bà Lê Kim T đang định cư ở nước ngoài.
57. Bà Lê Thị Đ đã có chỗ ở là nhà HSK, Phường 14, Quận 8.
58. Ông Lê Phú L và ông Lê Phú T hiện nay chưa sở hữu một căn nhà nào khác.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 659. Phân chia di sản theo di chúc. 1. Việc phân chia di sản được thực hiện theo ý chí của người để lại di chúc; nếu di chúc không xác định rõ phần của từng người thừa kế thì di sản được chia đều cho những người được chỉ định trong di chúc, trừ trường hợp có thoả thuận khác. 2. Trường hợp di chúc xác định phân chia di sản theo hiện vật thì người thừa kế được nhận hiện vật kèm theo hoa lợi, lợi tức thu được từ hiện vật đó hoặc phải chịu phần giá trị của hiện vật bị giảm sút tính đến thời điểm phân chia di sản; nếu hiện vật bị tiêu huỷ do lỗi của người khác thì người thừa kế có quyền yêu cầu bồi thường thiệt hại. 3. Trường hợp di chúc chỉ xác định phân chia di sản theo tỷ lệ đối với tổng giá trị kh
3. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
4. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
5. [BLDS 2015] Điều 656. Họp mặt những người thừa kế. 1. Sau khi có thông báo về việc mở thừa kế hoặc di chúc được công bố, những người thừa kế có thể họp mặt để thoả thuận những việc sau đây: a) Cử người quản lý di sản, người phân chia di sản, xác định quyền, nghĩa vụ của những người này, nếu người để lại di sản không chỉ định trong di chúc; b) Cách thức phân chia di sản. 2. Mọi thoả thuận của những người thừa kế phải được lập thành văn bản
Please suggest hypotheses to support why the outcome of the case might be the court rejects all of the plaintiff's claims.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng yếu tố trong vụ kiện này dựa trên các quy định pháp luật Việt Nam. Dựa trên thông tin cung cấp, tôi đưa ra một số giả thuyết có thể giúp hiểu rõ hơn về khả năng chấp nhận hoặc từ chối yêu cầu của nguyên đơn:

1. Yêu cầu chia tài sản nhà đất MC:
- Theo Điều 651 BLDS 2015, hàng thừa kế thứ nhất gồm vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi. Ông Lê Phú T là con trai của ông Lê Văn S và bà Ngô Thị N, nên ông thuộc hàng thừa kế thứ nhất.
- Tuy nhiên, ông Lê Phú T không đồng ý chia tài sản và yêu cầu chỉ chia cho 2 người con trai là ông L và ông T. Điều này có thể gây khó khăn cho việc chia tài sản.

2. Yêu cầu chia tài sản nhà đất HSK:
- Theo thông tin, nhà HSK là tài sản riêng của bà Lê Thị Đ, không phải di sản của ông S và bà N.
- Ông Lê Phú L yêu cầu chia phần nhà đất HSK, nhưng bị bà Lê Thị Đ bác bỏ.

3. Yêu cầu về sửa chữa nhà MC:
- Bà Lê Kim T đã chi 200 triệu đồng để sửa chữa nhà MC, nhưng không có hóa đơn chứng minh.
- Bà Lê Kim T không yêu cầu bồi thường số tiền này, nhưng ông Lê Phú L yêu cầu.

4. Yêu cầu về tài sản vật dụng trong nhà:
- Có một số tài sản vật dụng được xác định là di sản của ông S và bà N, nhưng không có thỏa thuận cụ thể về việc chia tài sản này.

5. Yêu cầu về việc quản lý di sản:
- Ông Lê Phú L và bà Lê Thị Đ đã thỏa thuận chia tài sản, nhưng không có thỏa thuận về việc quản lý di sản.

Giả thuyết có thể giúp lý giải rằng yêu cầu của nguyên đơn có thể không được chấp nhận:

- Yêu cầu chia tài sản nhà đất MC và nhà đất HSK có thể bị bác bỏ vì không tuân theo quy định về hàng thừa kế và tài sản di sản.
- Yêu cầu về sửa chữa nhà MC có thể bị bác bỏ vì không có hóa đơn chứng minh.
- Yêu cầu về tài sản vật dụng trong nhà có thể bị bác bỏ nếu không có thỏa thuận cụ thể về việc chia tài sản này.
- Yêu cầu về việc quản lý di sản có thể bị bác bỏ nếu không có thỏa thuận cụ thể về việc quản lý di sản.

Tóm lại, các yêu cầu của nguyên đơn có thể không được chấp nhận vì nhiều lý do liên quan
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
- outcome: **the court accepts the plaintiff's claims in whole or in part**
- converged: True
- accepted hypotheses: