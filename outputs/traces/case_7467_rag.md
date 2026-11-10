# Civil law simulation

## A.1 — rule_based

**Prompt**
```
Considering the following facts:
1. Tại đơn khởi kiện, bản tự khai, các biên bản lấy lời khai và tại phiên tòa bà Võ Thị Huỳnh H1 là nguyên đơn, đồng thời là đại diện theo ủy quyền của các đồng nguyên đơn (gồm bà Võ Thị Huỳnh H2, bà Võ Thị Thanh H5, bà Võ Thị Thanh H6, ông Võ Thế H3, ông Võ Thế H4) trình bày:
2. Cụ Võ Văn M, sinh năm 1916, chết ngày 13/10/2004 và cụ Phan Thị S, sinh năm 1919, chết ngày 15/11/2014 chung sống với nhau có tất cả 05 người con gồm:
3. 1. Ông Võ Thế A, sinh năm 1943, chết ngày 12/9/2015;
4. 2. Ông Võ Thế C, sinh năm 1946, chết ngày 15/6/2001, có vợ không con;
5. 3. Ông Võ Thế Đ, sinh năm 1948;
6. 4. Ông Võ Thế L, sinh năm 1953, chết ngày 31/1/2004, không có vợ con;
7. 5. Bà Võ Thị Cúc A, sinh năm 1960.
8. Ngoài ra, cụ M và cụ S không còn người con nào khác.
9. Đối với ông Võ Thế A (chết năm 2015) chung sống với bà Trần Thị V, sinh năm 1942, có tất cả 06 người con gồm:
10. 1. Bà Võ Thị Huỳnh H1, sinh năm 1964;
11. 2. Bà Võ Thị Huỳnh H2, sinh năm 1966;
12. 3. Ông Võ Thế H3, sinh năm 1967;
13. 4. Chị Võ Thị Khánh H4, sinh năm 1970;
14. 5. Anh Võ Thế H5, sinh năm 1972;
15. 6. Chị Võ Thị Thanh H6, sinh năm 1974.
16. Ngoài ra, ông A và bà V không còn người con nào khác.
17. Đối với ông Võ Thế C, chết năm 2001, có vợ bà Vương Thị Đ2, không có con. Trong vụ án này, bà Trần Thị V, bà Vương Thị Đ2 có đơn xin khước từ quyền thừa kế và xin từ chối tham gia tố tụng.
18. Lúc còn sống, cụ M và cụ S có tạo lập tài sản gồm:
19. 1. Đất:
20. Phần đất, thửa 443, diện tích 1.012m² và thửa 444, diện tích 875m², diện tích tổng cộng 1.887m² cùng tờ bản đồ số 01, tọa lạc tại ấp T, xã Q, Thị xã S (nay là khóm T, phường A, thành phố S) do cụ Phan Thị S đứng tên giấy chứng nhận quyền sử dụng đất (QSD đất) vào ngày 24/8/1993. Đến năm 2003 UBND TX S thu hồi làm đường N gồm: thửa 444, diện tích 92,3m², diện tích còn lại 794,7m². Đến năm 2006 tiếp tục thu hồi làm đường N gồm: thửa 444, diện tích 346,06m², loại đất T; thửa 443, diện …
21. Đến năm 1998, cụ M có cho bà H1 một phần đất ngang 7m, dài 20m, diện tích 140m² trong phần đất thửa 445, diện tích qua đo đạc thực tế 514,8m². Khi cho, cụ M và cụ S có ký tên vào đơn xin cất nhà của cha bà H1 là Võ Thế A (ông Anh làm đơn xin cất nhà cho bà H1), được UBND xã T xác nhận việc cụ M, cụ S cho đất bà H1. Bà H1 trình bày có đưa 02 lượng vàng 24k cho cụ M, cụ S để sửa chữa cất nhà. Bà H1 đã cất nhà lợp tole, vách tole, nền xi măng và gạch bông trên phần đất ở cho đến nay. Phần đất …
22. 2. Nhà:
23. Căn nhà tại số 539, trên thửa đất 443, nhà ngang khoảng 8m, dài khoảng 10m, máy lợp tole, tường gạch, nền gạch men và gạch tàu;
24. Hiện nay toàn bộ phần đất và căn nhà trên đất do ông Đ đang quản lý, sử dụng. Phần bà H1 chỉ sử dụng phần đất cụ M và cụ S cho cất nhà. Đối với Tờ di chúc cụ Phan Thị S lập ngày 31/01/2007, cụ S để lại toàn bộ QSD đất thửa 443 và thửa 444, diện tích 866,3m2, cùng tờ bản đồ 01 và căn nhà gắn liền với đất thửa 443 cho ông Võ Thế Đời được thừa hưởng, được Phòng Công chứng số X tỉnh Đồng Tháp công chứng. Theo bà H1 Tờ di chúc trên là không hợp pháp do không đúng quy định pháp luật vì tài sản …
25. - Thửa 444, diện tích: 365,1m2 gồm: H5 (DT: 121,7m2), H6 (DT: 121,7m2), H7 (DT: 121,7m2).
26. - Thửa 443, diện tích: 279,8m2 gồm: H9 (DT: 139,9m2) và H10 (DT: 139,9m2).
27. - Một phần Thửa 444 và một phần 443, diện tích: 139,9 m2 gồm: H8 (DT: 139,9m2),
28. Trong đó:
29. 1. Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444, diện tích 866,3m2, qua đo đạc thì diện tích thực tế là 784,8m2, ít hơn quyền sử dụng đất được cấp là 81,5m2. Thể hiện tại H5, H6, H7, H8, H9 và H10 (Thửa 444, diện tích 365,1m2 thuộc H5, H6, H7 và 01 phần H8; Thửa 443, diện tích 279,8m2 thuộc H9, H10 và 01 phần H8).
30. 2. Phần đất chưa được cấp quyền sử dụng đất thửa 445 tờ bản đồ số 1 diện tích 514,8m2, thể hiện tại H1,H2,H3,H4. Tại H4 (DT: 153,6m2), có căn nhà của bà H1 đang quản lý, sử dụng. Nguồn gốc đất là bà H1 được cụ M và cụ S tặng cho phần đất diện tích 153,6m2 để xây dựng nhà ở. Vì vậy, khi chia thừa kế, bà H1 yêu cầu trừ ra phần diện tích 153,6m2 mà cụ M, cụ S đã cho riêng bà H1 nên diện tích còn lại: 361,2m2.
31. Bà H1 xác định tờ di chúc của cụ M lập không hợp pháp nên toàn bộ di sản của cụ M và cụ S sẽ yêu cầu chia thừa kế theo pháp luật.
32. Nay bà Võ Thị Huỳnh H1 yêu cầu chia thừa kế theo pháp luật di sản của cụ M và cụ S cụ thể:
33. 1. Về người được hưởng thừa kế: cụ M và cụ S có 05 người con nhưng 02 người chết, không có vợ con nên 03 người còn lại được hưởng thừa kế là: Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau.
34. 2. Di sản chia thừa kế:
35. - Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444 theo diện tích thực tế là 784,8m2 và phần đất chưa được cấp quyền sử dụng đất thửa 445 theo diện tích thực tế là 514,8m2, tổng cộng diện tích là 1.299,6m2 nhưng trừ lại 153,6m2 (Cụ M, cụ S cho bà H1) còn lại diện tích 1.146m2 chia thành 03 phần bằng nhau. Vậy mỗi phần diện tích là 382m2, cụ thể: ông Võ Thế A chết nên các con ông A là bà H1 và các đồng nguyên đơn 01 phần diện tích đất là 382m2; ông Võ Thế Đ 01 phần diện tích đất là …
36. - Về cách chia: cụ thể:
37. + Phần bà H1: được nhận diện tích là 382m2 đất thể hiện tại H3, H5, H8, tổng diện tích 382m2.
38. Đối với phần diện tích 382m2 được chia thì bà H1 không yêu cầu chia cụ thể cho các đồng nguyên đơn; giữa bà H1 và các đồng nguyên đơn sẽ tự thỏa thuận phân chia với nhau.
39. + Phần ông Đ: được nhận diện tích là 382m2 đất thể hiện tại H1, H7 và H10.
40. + Phần bà Cúc A: được nhận diện tích là 382m2 đất thể hiện tại thể hiện tại H2, H6 và H9.
41. Bà H1 đồng ý bồi thường các tài sản và cây trồng trên phần đất được nhận  theo định giá cho ông Đ cụ thể:
42. - Căn nhà kho (tại H8) trị giá 45.294.480đ;
43. - 03 cây dừa (tại H5) giá trị 1.020.000đ
44. - 04 cây dừa (tại H8) giá trị 1.360.000đ.
45. Tổng cộng bà H1 đồng ý bồi thường cho ông Đ số tiền 47.674.000đ.
46. Bà H1 được quyền sở hữu nhà kho và các cây trồng trên.
47. Trong trường hợp xác định di chúc có hiệu lực thì bà H1 yêu cầu chia thừa kế quyền sử dụng đất thửa 445, hiện chưa được cấp giấy chứng nhận QSD đất thể hiện tại H1, H2, H3 và H4, tổng diện tích 514,8m2 nhưng phải trừ ra diện tích H4 là 153,6m2 mà cụ M, bà Su đã tặng cho bà H1. Còn lại H1, H2 và H3 diện tích là 361,2m2 thì chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, diện tích 120,4m2. Vị trí đất chia do Tòa án …
48. Đối với căn nhà, tài sản khác và các cây trồng trên đất của cụ M và cụ S theo định giá thì bà H1 không yêu cầu chia thừa kế. Tại phiên tòa, bà H1 đồng ý giao cho ông Đ được quyền sở hữu tài sản trên đất là nhà, các cây trồng và các tài sản khác trên đất. Ngoài ra, bà H1 không có yêu cầu gì khác.
49. Tại bản tự khai, các biên bản lấy lời khai và tại phiên tòa bị đơn ông Võ Thế Đ trình bày:  Ông Đ xác định: Cụ Võ Văn M, sinh năm 1916, chết năm 2004 và cụ Phan Thị S, sinh năm 1919, chết năm 2014 chung sống với nhau có tất cả 05 người con theo như bà H1 trình bày là đúng. Đối với tài sản cụ M và cụ S trước đây có chia cho ông Võ Thế A đất ruộng và đất nền nhà, đồng thời ông Đ đã cho tiền cho anh Thế H (con của ông Thế A) xong, còn lại phần đất thửa 443 và 444, cùng tờ bản đồ số 01 là cấp …
50. Trên phần đất thửa 443 có căn nhà số 539 thể hiện tại H10 trên sơ đồ đo đạc ngày 07/7/2017 là căn nhà thờ đã có từ ba đời nay để thờ cúng ông bà, hiện ông Đ là người trực tiếp quản lý sử dụng nhà. Ông Đ xác định: cụ M và cụ S không có cho bà H1 phần đất cất nhà ngang 7m và dài 20m, diện tích thực tế là 153,6m2 thuộc thửa 445 thể hiện tại H4 trên Sơ đồ đo đạc, giấy tờ là do bà H1 giả mạo, thực tế cụ M và cụ S không có ký, ông Đ không yêu cầu giám định. Phần đất bà H1 đang sử dụng cất nhà ở …
51. Nay ông Võ Thế Đ không đồng ý chia thừa kế theo yêu cầu khởi kiện của các nguyên đơn. Ông Đ yêu cầu được thừa hưởng toàn bộ tài sản: đất, nhà và cây trồng trên đất theo nội dung Tờ di chúc ngày ngày 31/01/2007 của cụ Phan Thị S (bao gồm diện tích theo giấy chứng nhận quyền sử dụng đất là 866,3m2, diện tích thực tế là 1.299,6m2). Trong trường hợp xác định di chúc có hiệu lực của thửa 443,444 còn thửa 445 trường hợp chia thừa kế phần đất hiện chưa được cấp giấy chứng nhận QSD đất thể hiện …
52. Người có quyền lợi, nghĩa vụ liên quan bà Võ Thị Cúc A (ủy quyền cho ông Võ Thế Đ) và bà Lê Thị Thanh Đ1 trình bày:
53. Bà Cúc A và bà Đ1 đồng ý theo ý kiến trình bày và yêu cầu của ông Đ. Ngoài ra, bà Cúc A và bà Đ1 không có yêu cầu gì khác. Đối với bà Cúc A1 xác định trường hợp chia thừa kế thì phần bà Cúc A được hưởng cho lại ông Đ để thờ cúng ông bà.
54. Người có quyền lợi, nghĩa vụ liên quan Ủy ban nhân dân thành phố S ủy quyền cho ông Nguyễn Văn H có ý kiến như sau:
55. Ngày 24/8/1993, Ủy ban nhân dân thành phố S cấp giấy chứng nhận QSD đất thửa 443 và thửa 444, cùng tờ bản đồ số 01 là cấp cho cá nhân bà Phan Thị S. Phần đất tranh chấp thể hiện tại các hình H1, H2, H3 và H4 theo sơ đồ đo đạc ngày 07/7/2017 thuộc thửa 445, tờ bản đồ 01, mục đích sử dụng: T, chưa được cấp giấy chứng nhận là của ông Võ Văn M.
56. Qua đối chiếu giữa hai hệ thống bản đồ địa chính thì H5, H6, H7 thuộc một phần thửa 444, tờ bản đồ số 01; H8 có một phần thuộc thửa 444 và một phần thuộc thửa 443; H9 và H10 thuộc một phần thửa 443, tờ bản đồ số 01 đã được cấp giấy chứng nhận QSD đất cho bà Phan Thị S. Nguyên nhân diện tích đo đạc thực tế từ H5 đến H10 thiếu 81,5m2 so với diện tích cấp giấy chứng nhận QSD đất là do cụ S kê khai đăng ký không chính xác, khi cấp giấy không có đo đạc diện tích thực tế.
57. Ngoài ra, Ủy ban không có ý kiến gì thêm.
58. * Người có quyền lợi, nghĩa vụ liên quan Phòng Công chứng số X tỉnh Đồng Tháp ủy quyền cho ông Đỗ Công K có ý kiến:
59. Ngày 31/01/2007, công chứng viên Đỗ Công K – thuộc Phòng Công chứng số X – tỉnh Đồng Tháp, có công chứng Tờ di chúc cho bà Phan Thị S, với nội dung sau khi bà S chết quyền sử dụng đất theo giấy chứng nhận QSD đất số B236994 do UBND thị xã S (nay là thành phố S) cấp ngày 24/8/1993 để lại cho ông Võ Thế Đ thừa hưởng. Sau khi kiểm tra hồ sơ lưu giữ tại Phòng Công chứng số X và đối chiếu với quy định của pháp luật, xác định công chứng viên Đỗ Công K, công chứng Tờ di chúc cho bà Phan Thị S để …
60. * Đại diện Viện kiểm sát nhân dân thành phố S phát biểu ý kiến:
61. - Về thủ tục tố tụng: Việc tuân theo pháp luật tố tụng của Thẩm phán, Hội đồng xét xử và Thư ký phiên tòa trong quá trình giải quyết vụ án, kể từ khi thụ lý cho đến trước thời điểm Hội đồng xét xử nghị án đảm bảo đúng theo quy định.
62. - Về nội dung:
63. Qua nghiên cứu hồ sơ vụ án, tại phiên tòa nhận thấy:
64. - Đối với việc bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444, nhận thấy: Theo đơn đăng ký quyền sử dụng ruộng đất ngày 22/10/1991 cụ S thể hiện nguồn gốc đất là của bà Tiêu Thị T mẹ bà S chết để lại và theo GCNQSDĐ  cấp
65. cho cụ S vào ngày 24/8/1993  là cấp cho cá nhân cụ S. Tại thời điểm đăng ký và GCNQSDĐ cụ M còn sống, từ khi cấp QSD đất cho đến nay bà S chưa cấp đổi, cụ S và cụ M chưa văn bản giấy tờ gì xác nhận phần đất này là tài sản chung của cụ M
66. và cụ S. Do đó, bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444 là tài sản chung cụ M là không có cơ sở.
67. Ngày 31/01/2007 cụ S lập di chúc để lại toàn bộ thửa 443 và thửa 444, theo GCNQSD đất cho ông Võ Thế Đ được thửa hưởng. Tờ Di chúc được được Phòng Công chứng số X tỉnh Đồng Tháp công chứng nên di chúc hợp pháp theo điều 652 BLDS, do đó bà H1 yêu cầu chia thừa kế phần đất thửa 443 và thửa 444 diện tích 784.8m2 là không có căn cứ nên đề nghị Hội đồng xét xử không chấp nhận yêu cầu bà H1.
68. - Đối với thửa 445 các đương sự thừa nhận là đất của cụ M, cụ S sử dụng ổn định lâu dài từ trước năm 1993 cho đến khi cụ S chết 2014. UBND thành phố S xác định thửa đất này chưa được cấp quyền sử dụng đất cho ai và cụ M và cụ S là người quản lý sử dụng từ trước năm 1993 cho đến nay. Đến khi cụ S chết có để lại di chúc nhưng trong di chúc không thể hiện việc định đoạt thửa đất 445. Do đó, thửa 445 là di sản của cụ M và cụ S được chia đều cho các đồng thừa kế thuộc hàng thừa kế thứ nhất theo …
69. -  Theo các tài liệu xác định cụ M và cụ S có 05 người con . Về người được hưởng thừa kế :Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau được các đương sự thừa nhận căn cú khoản 2 điều 92 BLTTDS thì tình tiết này không phải chứng minh nên đề nghị Hội đồng xét xử chấp nhận. Bà H1 yêu cầu chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, …
70. - Về phần đất diện tích H4 là 153,6m2 bà H1 và ông Đ không có yêu cầu giải quyết trong vụ kiện này nên đề nghị Hội đồng xét xử không xem xét.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
3. [BLDS 2015] Điều 617. Nghĩa vụ của người quản lý di sản. 1. Người quản lý di sản quy định tại khoản 1 và khoản 3 Điều 616 của Bộ luật này có nghĩa vụ sau đây: a) Lập danh mục di sản; thu hồi tài sản thuộc di sản của người chết mà người khác đang chiếm hữu, trừ trường hợp pháp luật có quy định khác; b) Bảo quản di sản; không được bán, trao đổi, tặng cho, cầm cố, thế chấp hoặc định đoạt tài sản bằng hình thức khác, nếu không được những người thừa kế đồng ý bằng văn bản; c) Thông báo về tình trạng di sản cho những người thừa kế; d) Bồi thường thiệt hại nếu vi phạm nghĩa vụ của mình mà gây thiệt hại; đ) Giao lại di sản theo yêu cầu của người thừa kế. 2. Người đang chiếm hữu, sử dụng, quản lý di sản quy định tại khoản
4. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
5. [BLDS 2015] Điều 645. Di sản dùng vào việc thờ cúng. 1. Trường hợp người lập di chúc để lại một phần di sản dùng vào việc thờ cúng thì phần di sản đó không được chia thừa kế và được giao cho người đã được chỉ định trong di chúc quản lý để thực hiện việc thờ cúng; nếu người được chỉ định không thực hiện đúng di chúc hoặc không theo thoả thuận của những người thừa kế thì những người thừa kế có quyền giao phần di sản dùng vào việc thờ cúng cho người khác quản lý để thờ cúng. Trường hợp người để lại di sản không chỉ định người quản lý di sản thờ cúng thì những người thừa kế cử người quản lý di sản thờ cúng. Trường hợp tất cả những người thừa kế theo di chúc đều đã chết thì phần di sản dùng để thờ cúng thuộc về người 
According to the given rules, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để đánh giá yêu cầu của nguyên đơn có được chấp nhận hay không, chúng ta cần phân tích từng phần yêu cầu của bà Võ Thị Huỳnh H1:

1. **Phần đất thửa 443 và 444:** 
   - Theo quy định tại Điều 651 BLDS 2015, bà H1 không có cơ sở yêu cầu chia thừa kế phần đất này vì nó không phải là tài sản chung của cụ M và cụ S. 
   - Điều 662 BLDS 2015 cũng không cho phép phân chia lại di sản nếu đã phân chia và không có người thừa kế mới.

2. **Phần đất thửa 445:** 
   - Bà H1 yêu cầu chia phần đất này nhưng không có cơ sở pháp lý vì phần đất này chưa được cấp giấy chứng nhận quyền sử dụng đất và không có di chúc xác định phân chia.
   - Theo Điều 660 BLDS 2015, nếu không thể chia bằng hiện vật, bà H1 không có quyền yêu cầu phân chia.

3. **Tờ di chúc của cụ Phan Thị S:** 
   - Bà H1 yêu cầu xác định tính hợp pháp của tờ di chúc này. Theo Điều 652 BLDS 2015, nếu Tờ di chúc được công chứng hợp pháp, thì bà H1 không có quyền yêu cầu chia thừa kế theo yêu cầu của bà H1.

4. **Các tài sản khác:** 
   - Bà H1 không yêu cầu chia tài sản khác như nhà, cây trồng, nên không có vấn đề gì.

Từ phân tích trên, yêu cầu của bà Võ Thị Huỳnh H1 không có cơ sở pháp lý và không được chấp nhận.

Yêu cầu của nguyên đơn không được chấp nhận.
```

## A.2#1 — abductive (plaintiff)

**Prompt**
```
Considering the following facts:
1. Tại đơn khởi kiện, bản tự khai, các biên bản lấy lời khai và tại phiên tòa bà Võ Thị Huỳnh H1 là nguyên đơn, đồng thời là đại diện theo ủy quyền của các đồng nguyên đơn (gồm bà Võ Thị Huỳnh H2, bà Võ Thị Thanh H5, bà Võ Thị Thanh H6, ông Võ Thế H3, ông Võ Thế H4) trình bày:
2. Cụ Võ Văn M, sinh năm 1916, chết ngày 13/10/2004 và cụ Phan Thị S, sinh năm 1919, chết ngày 15/11/2014 chung sống với nhau có tất cả 05 người con gồm:
3. 1. Ông Võ Thế A, sinh năm 1943, chết ngày 12/9/2015;
4. 2. Ông Võ Thế C, sinh năm 1946, chết ngày 15/6/2001, có vợ không con;
5. 3. Ông Võ Thế Đ, sinh năm 1948;
6. 4. Ông Võ Thế L, sinh năm 1953, chết ngày 31/1/2004, không có vợ con;
7. 5. Bà Võ Thị Cúc A, sinh năm 1960.
8. Ngoài ra, cụ M và cụ S không còn người con nào khác.
9. Đối với ông Võ Thế A (chết năm 2015) chung sống với bà Trần Thị V, sinh năm 1942, có tất cả 06 người con gồm:
10. 1. Bà Võ Thị Huỳnh H1, sinh năm 1964;
11. 2. Bà Võ Thị Huỳnh H2, sinh năm 1966;
12. 3. Ông Võ Thế H3, sinh năm 1967;
13. 4. Chị Võ Thị Khánh H4, sinh năm 1970;
14. 5. Anh Võ Thế H5, sinh năm 1972;
15. 6. Chị Võ Thị Thanh H6, sinh năm 1974.
16. Ngoài ra, ông A và bà V không còn người con nào khác.
17. Đối với ông Võ Thế C, chết năm 2001, có vợ bà Vương Thị Đ2, không có con. Trong vụ án này, bà Trần Thị V, bà Vương Thị Đ2 có đơn xin khước từ quyền thừa kế và xin từ chối tham gia tố tụng.
18. Lúc còn sống, cụ M và cụ S có tạo lập tài sản gồm:
19. 1. Đất:
20. Phần đất, thửa 443, diện tích 1.012m² và thửa 444, diện tích 875m², diện tích tổng cộng 1.887m² cùng tờ bản đồ số 01, tọa lạc tại ấp T, xã Q, Thị xã S (nay là khóm T, phường A, thành phố S) do cụ Phan Thị S đứng tên giấy chứng nhận quyền sử dụng đất (QSD đất) vào ngày 24/8/1993. Đến năm 2003 UBND TX S thu hồi làm đường N gồm: thửa 444, diện tích 92,3m², diện tích còn lại 794,7m². Đến năm 2006 tiếp tục thu hồi làm đường N gồm: thửa 444, diện tích 346,06m², loại đất T; thửa 443, diện …
21. Đến năm 1998, cụ M có cho bà H1 một phần đất ngang 7m, dài 20m, diện tích 140m² trong phần đất thửa 445, diện tích qua đo đạc thực tế 514,8m². Khi cho, cụ M và cụ S có ký tên vào đơn xin cất nhà của cha bà H1 là Võ Thế A (ông Anh làm đơn xin cất nhà cho bà H1), được UBND xã T xác nhận việc cụ M, cụ S cho đất bà H1. Bà H1 trình bày có đưa 02 lượng vàng 24k cho cụ M, cụ S để sửa chữa cất nhà. Bà H1 đã cất nhà lợp tole, vách tole, nền xi măng và gạch bông trên phần đất ở cho đến nay. Phần đất …
22. 2. Nhà:
23. Căn nhà tại số 539, trên thửa đất 443, nhà ngang khoảng 8m, dài khoảng 10m, máy lợp tole, tường gạch, nền gạch men và gạch tàu;
24. Hiện nay toàn bộ phần đất và căn nhà trên đất do ông Đ đang quản lý, sử dụng. Phần bà H1 chỉ sử dụng phần đất cụ M và cụ S cho cất nhà. Đối với Tờ di chúc cụ Phan Thị S lập ngày 31/01/2007, cụ S để lại toàn bộ QSD đất thửa 443 và thửa 444, diện tích 866,3m2, cùng tờ bản đồ 01 và căn nhà gắn liền với đất thửa 443 cho ông Võ Thế Đời được thừa hưởng, được Phòng Công chứng số X tỉnh Đồng Tháp công chứng. Theo bà H1 Tờ di chúc trên là không hợp pháp do không đúng quy định pháp luật vì tài sản …
25. - Thửa 444, diện tích: 365,1m2 gồm: H5 (DT: 121,7m2), H6 (DT: 121,7m2), H7 (DT: 121,7m2).
26. - Thửa 443, diện tích: 279,8m2 gồm: H9 (DT: 139,9m2) và H10 (DT: 139,9m2).
27. - Một phần Thửa 444 và một phần 443, diện tích: 139,9 m2 gồm: H8 (DT: 139,9m2),
28. Trong đó:
29. 1. Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444, diện tích 866,3m2, qua đo đạc thì diện tích thực tế là 784,8m2, ít hơn quyền sử dụng đất được cấp là 81,5m2. Thể hiện tại H5, H6, H7, H8, H9 và H10 (Thửa 444, diện tích 365,1m2 thuộc H5, H6, H7 và 01 phần H8; Thửa 443, diện tích 279,8m2 thuộc H9, H10 và 01 phần H8).
30. 2. Phần đất chưa được cấp quyền sử dụng đất thửa 445 tờ bản đồ số 1 diện tích 514,8m2, thể hiện tại H1,H2,H3,H4. Tại H4 (DT: 153,6m2), có căn nhà của bà H1 đang quản lý, sử dụng. Nguồn gốc đất là bà H1 được cụ M và cụ S tặng cho phần đất diện tích 153,6m2 để xây dựng nhà ở. Vì vậy, khi chia thừa kế, bà H1 yêu cầu trừ ra phần diện tích 153,6m2 mà cụ M, cụ S đã cho riêng bà H1 nên diện tích còn lại: 361,2m2.
31. Bà H1 xác định tờ di chúc của cụ M lập không hợp pháp nên toàn bộ di sản của cụ M và cụ S sẽ yêu cầu chia thừa kế theo pháp luật.
32. Nay bà Võ Thị Huỳnh H1 yêu cầu chia thừa kế theo pháp luật di sản của cụ M và cụ S cụ thể:
33. 1. Về người được hưởng thừa kế: cụ M và cụ S có 05 người con nhưng 02 người chết, không có vợ con nên 03 người còn lại được hưởng thừa kế là: Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau.
34. 2. Di sản chia thừa kế:
35. - Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444 theo diện tích thực tế là 784,8m2 và phần đất chưa được cấp quyền sử dụng đất thửa 445 theo diện tích thực tế là 514,8m2, tổng cộng diện tích là 1.299,6m2 nhưng trừ lại 153,6m2 (Cụ M, cụ S cho bà H1) còn lại diện tích 1.146m2 chia thành 03 phần bằng nhau. Vậy mỗi phần diện tích là 382m2, cụ thể: ông Võ Thế A chết nên các con ông A là bà H1 và các đồng nguyên đơn 01 phần diện tích đất là 382m2; ông Võ Thế Đ 01 phần diện tích đất là …
36. - Về cách chia: cụ thể:
37. + Phần bà H1: được nhận diện tích là 382m2 đất thể hiện tại H3, H5, H8, tổng diện tích 382m2.
38. Đối với phần diện tích 382m2 được chia thì bà H1 không yêu cầu chia cụ thể cho các đồng nguyên đơn; giữa bà H1 và các đồng nguyên đơn sẽ tự thỏa thuận phân chia với nhau.
39. + Phần ông Đ: được nhận diện tích là 382m2 đất thể hiện tại H1, H7 và H10.
40. + Phần bà Cúc A: được nhận diện tích là 382m2 đất thể hiện tại thể hiện tại H2, H6 và H9.
41. Bà H1 đồng ý bồi thường các tài sản và cây trồng trên phần đất được nhận  theo định giá cho ông Đ cụ thể:
42. - Căn nhà kho (tại H8) trị giá 45.294.480đ;
43. - 03 cây dừa (tại H5) giá trị 1.020.000đ
44. - 04 cây dừa (tại H8) giá trị 1.360.000đ.
45. Tổng cộng bà H1 đồng ý bồi thường cho ông Đ số tiền 47.674.000đ.
46. Bà H1 được quyền sở hữu nhà kho và các cây trồng trên.
47. Trong trường hợp xác định di chúc có hiệu lực thì bà H1 yêu cầu chia thừa kế quyền sử dụng đất thửa 445, hiện chưa được cấp giấy chứng nhận QSD đất thể hiện tại H1, H2, H3 và H4, tổng diện tích 514,8m2 nhưng phải trừ ra diện tích H4 là 153,6m2 mà cụ M, bà Su đã tặng cho bà H1. Còn lại H1, H2 và H3 diện tích là 361,2m2 thì chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, diện tích 120,4m2. Vị trí đất chia do Tòa án …
48. Đối với căn nhà, tài sản khác và các cây trồng trên đất của cụ M và cụ S theo định giá thì bà H1 không yêu cầu chia thừa kế. Tại phiên tòa, bà H1 đồng ý giao cho ông Đ được quyền sở hữu tài sản trên đất là nhà, các cây trồng và các tài sản khác trên đất. Ngoài ra, bà H1 không có yêu cầu gì khác.
49. Tại bản tự khai, các biên bản lấy lời khai và tại phiên tòa bị đơn ông Võ Thế Đ trình bày:  Ông Đ xác định: Cụ Võ Văn M, sinh năm 1916, chết năm 2004 và cụ Phan Thị S, sinh năm 1919, chết năm 2014 chung sống với nhau có tất cả 05 người con theo như bà H1 trình bày là đúng. Đối với tài sản cụ M và cụ S trước đây có chia cho ông Võ Thế A đất ruộng và đất nền nhà, đồng thời ông Đ đã cho tiền cho anh Thế H (con của ông Thế A) xong, còn lại phần đất thửa 443 và 444, cùng tờ bản đồ số 01 là cấp …
50. Trên phần đất thửa 443 có căn nhà số 539 thể hiện tại H10 trên sơ đồ đo đạc ngày 07/7/2017 là căn nhà thờ đã có từ ba đời nay để thờ cúng ông bà, hiện ông Đ là người trực tiếp quản lý sử dụng nhà. Ông Đ xác định: cụ M và cụ S không có cho bà H1 phần đất cất nhà ngang 7m và dài 20m, diện tích thực tế là 153,6m2 thuộc thửa 445 thể hiện tại H4 trên Sơ đồ đo đạc, giấy tờ là do bà H1 giả mạo, thực tế cụ M và cụ S không có ký, ông Đ không yêu cầu giám định. Phần đất bà H1 đang sử dụng cất nhà ở …
51. Nay ông Võ Thế Đ không đồng ý chia thừa kế theo yêu cầu khởi kiện của các nguyên đơn. Ông Đ yêu cầu được thừa hưởng toàn bộ tài sản: đất, nhà và cây trồng trên đất theo nội dung Tờ di chúc ngày ngày 31/01/2007 của cụ Phan Thị S (bao gồm diện tích theo giấy chứng nhận quyền sử dụng đất là 866,3m2, diện tích thực tế là 1.299,6m2). Trong trường hợp xác định di chúc có hiệu lực của thửa 443,444 còn thửa 445 trường hợp chia thừa kế phần đất hiện chưa được cấp giấy chứng nhận QSD đất thể hiện …
52. Người có quyền lợi, nghĩa vụ liên quan bà Võ Thị Cúc A (ủy quyền cho ông Võ Thế Đ) và bà Lê Thị Thanh Đ1 trình bày:
53. Bà Cúc A và bà Đ1 đồng ý theo ý kiến trình bày và yêu cầu của ông Đ. Ngoài ra, bà Cúc A và bà Đ1 không có yêu cầu gì khác. Đối với bà Cúc A1 xác định trường hợp chia thừa kế thì phần bà Cúc A được hưởng cho lại ông Đ để thờ cúng ông bà.
54. Người có quyền lợi, nghĩa vụ liên quan Ủy ban nhân dân thành phố S ủy quyền cho ông Nguyễn Văn H có ý kiến như sau:
55. Ngày 24/8/1993, Ủy ban nhân dân thành phố S cấp giấy chứng nhận QSD đất thửa 443 và thửa 444, cùng tờ bản đồ số 01 là cấp cho cá nhân bà Phan Thị S. Phần đất tranh chấp thể hiện tại các hình H1, H2, H3 và H4 theo sơ đồ đo đạc ngày 07/7/2017 thuộc thửa 445, tờ bản đồ 01, mục đích sử dụng: T, chưa được cấp giấy chứng nhận là của ông Võ Văn M.
56. Qua đối chiếu giữa hai hệ thống bản đồ địa chính thì H5, H6, H7 thuộc một phần thửa 444, tờ bản đồ số 01; H8 có một phần thuộc thửa 444 và một phần thuộc thửa 443; H9 và H10 thuộc một phần thửa 443, tờ bản đồ số 01 đã được cấp giấy chứng nhận QSD đất cho bà Phan Thị S. Nguyên nhân diện tích đo đạc thực tế từ H5 đến H10 thiếu 81,5m2 so với diện tích cấp giấy chứng nhận QSD đất là do cụ S kê khai đăng ký không chính xác, khi cấp giấy không có đo đạc diện tích thực tế.
57. Ngoài ra, Ủy ban không có ý kiến gì thêm.
58. * Người có quyền lợi, nghĩa vụ liên quan Phòng Công chứng số X tỉnh Đồng Tháp ủy quyền cho ông Đỗ Công K có ý kiến:
59. Ngày 31/01/2007, công chứng viên Đỗ Công K – thuộc Phòng Công chứng số X – tỉnh Đồng Tháp, có công chứng Tờ di chúc cho bà Phan Thị S, với nội dung sau khi bà S chết quyền sử dụng đất theo giấy chứng nhận QSD đất số B236994 do UBND thị xã S (nay là thành phố S) cấp ngày 24/8/1993 để lại cho ông Võ Thế Đ thừa hưởng. Sau khi kiểm tra hồ sơ lưu giữ tại Phòng Công chứng số X và đối chiếu với quy định của pháp luật, xác định công chứng viên Đỗ Công K, công chứng Tờ di chúc cho bà Phan Thị S để …
60. * Đại diện Viện kiểm sát nhân dân thành phố S phát biểu ý kiến:
61. - Về thủ tục tố tụng: Việc tuân theo pháp luật tố tụng của Thẩm phán, Hội đồng xét xử và Thư ký phiên tòa trong quá trình giải quyết vụ án, kể từ khi thụ lý cho đến trước thời điểm Hội đồng xét xử nghị án đảm bảo đúng theo quy định.
62. - Về nội dung:
63. Qua nghiên cứu hồ sơ vụ án, tại phiên tòa nhận thấy:
64. - Đối với việc bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444, nhận thấy: Theo đơn đăng ký quyền sử dụng ruộng đất ngày 22/10/1991 cụ S thể hiện nguồn gốc đất là của bà Tiêu Thị T mẹ bà S chết để lại và theo GCNQSDĐ  cấp
65. cho cụ S vào ngày 24/8/1993  là cấp cho cá nhân cụ S. Tại thời điểm đăng ký và GCNQSDĐ cụ M còn sống, từ khi cấp QSD đất cho đến nay bà S chưa cấp đổi, cụ S và cụ M chưa văn bản giấy tờ gì xác nhận phần đất này là tài sản chung của cụ M
66. và cụ S. Do đó, bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444 là tài sản chung cụ M là không có cơ sở.
67. Ngày 31/01/2007 cụ S lập di chúc để lại toàn bộ thửa 443 và thửa 444, theo GCNQSD đất cho ông Võ Thế Đ được thửa hưởng. Tờ Di chúc được được Phòng Công chứng số X tỉnh Đồng Tháp công chứng nên di chúc hợp pháp theo điều 652 BLDS, do đó bà H1 yêu cầu chia thừa kế phần đất thửa 443 và thửa 444 diện tích 784.8m2 là không có căn cứ nên đề nghị Hội đồng xét xử không chấp nhận yêu cầu bà H1.
68. - Đối với thửa 445 các đương sự thừa nhận là đất của cụ M, cụ S sử dụng ổn định lâu dài từ trước năm 1993 cho đến khi cụ S chết 2014. UBND thành phố S xác định thửa đất này chưa được cấp quyền sử dụng đất cho ai và cụ M và cụ S là người quản lý sử dụng từ trước năm 1993 cho đến nay. Đến khi cụ S chết có để lại di chúc nhưng trong di chúc không thể hiện việc định đoạt thửa đất 445. Do đó, thửa 445 là di sản của cụ M và cụ S được chia đều cho các đồng thừa kế thuộc hàng thừa kế thứ nhất theo …
69. -  Theo các tài liệu xác định cụ M và cụ S có 05 người con . Về người được hưởng thừa kế :Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau được các đương sự thừa nhận căn cú khoản 2 điều 92 BLTTDS thì tình tiết này không phải chứng minh nên đề nghị Hội đồng xét xử chấp nhận. Bà H1 yêu cầu chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, …
70. - Về phần đất diện tích H4 là 153,6m2 bà H1 và ông Đ không có yêu cầu giải quyết trong vụ kiện này nên đề nghị Hội đồng xét xử không xem xét.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
3. [BLDS 2015] Điều 617. Nghĩa vụ của người quản lý di sản. 1. Người quản lý di sản quy định tại khoản 1 và khoản 3 Điều 616 của Bộ luật này có nghĩa vụ sau đây: a) Lập danh mục di sản; thu hồi tài sản thuộc di sản của người chết mà người khác đang chiếm hữu, trừ trường hợp pháp luật có quy định khác; b) Bảo quản di sản; không được bán, trao đổi, tặng cho, cầm cố, thế chấp hoặc định đoạt tài sản bằng hình thức khác, nếu không được những người thừa kế đồng ý bằng văn bản; c) Thông báo về tình trạng di sản cho những người thừa kế; d) Bồi thường thiệt hại nếu vi phạm nghĩa vụ của mình mà gây thiệt hại; đ) Giao lại di sản theo yêu cầu của người thừa kế. 2. Người đang chiếm hữu, sử dụng, quản lý di sản quy định tại khoản
4. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
5. [BLDS 2015] Điều 645. Di sản dùng vào việc thờ cúng. 1. Trường hợp người lập di chúc để lại một phần di sản dùng vào việc thờ cúng thì phần di sản đó không được chia thừa kế và được giao cho người đã được chỉ định trong di chúc quản lý để thực hiện việc thờ cúng; nếu người được chỉ định không thực hiện đúng di chúc hoặc không theo thoả thuận của những người thừa kế thì những người thừa kế có quyền giao phần di sản dùng vào việc thờ cúng cho người khác quản lý để thờ cúng. Trường hợp người để lại di sản không chỉ định người quản lý di sản thờ cúng thì những người thừa kế cử người quản lý di sản thờ cúng. Trường hợp tất cả những người thừa kế theo di chúc đều đã chết thì phần di sản dùng để thờ cúng thuộc về người 
Please suggest hypotheses to support why the outcome of the case might be the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Để xác định liệu yêu cầu của nguyên đơn có được chấp nhận hoàn toàn hay một phần, chúng ta cần phân tích từng yếu tố trong vụ kiện này dựa trên các quy định pháp luật Việt Nam:

1. **Nguyên tắc phân chia di sản theo pháp luật**:
   - Theo Điều 660 BLDS 2015, khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng. 
   - Trong vụ kiện này, cụ M và cụ S có 5 người con, trong đó 2 người đã chết. Do đó, việc phân chia di sản cần đảm bảo quyền lợi cho các con còn sống.

2. **Di sản chia thừa kế**:
   - Theo Điều 651 BLDS 2015, hàng thừa kế thứ nhất bao gồm vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết. 
   - Trong vụ kiện này, bà Võ Thị Huỳnh H1 là nguyên đơn và là đại diện cho các đồng nguyên đơn, trong đó có các con của ông Võ Thế A (vợ ông A là bà Trần Thị V, không có con).

3. **Tài sản chia thừa kế**:
   - Tài sản chia thừa kế bao gồm đất và nhà. 
   - Theo Điều 662 BLDS 2015, nếu đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận.

4. **Di sản dùng vào việc thờ cúng**:
   - Theo Điều 645 BLDS 2015, nếu người lập di chúc để lại một phần di sản dùng vào việc thờ cúng thì phần di sản đó không được chia thừa kế và được giao cho người đã được chỉ định trong di chúc quản lý để thực hiện việc thờ cúng.
   - Trong vụ kiện này, cụ M và cụ S đã để lại một phần đất dùng vào việc thờ cúng, nên phần đất này không được chia thừa kế.

5. **Phân chia tài sản cụ thể**:
   - Theo yêu cầu của bà H1, phần đất thửa 443 và 444 được chia thành 3 phần bằng nhau, mỗi phần 382m2.
   - Phần đất thửa
```

## judge#1 — judge

**Prompt**
```

```
**Response**
```
llm judge
```

## A.3#1 — rule_based (plaintiff)

**Prompt**
```
Considering the following facts:
1. Tại đơn khởi kiện, bản tự khai, các biên bản lấy lời khai và tại phiên tòa bà Võ Thị Huỳnh H1 là nguyên đơn, đồng thời là đại diện theo ủy quyền của các đồng nguyên đơn (gồm bà Võ Thị Huỳnh H2, bà Võ Thị Thanh H5, bà Võ Thị Thanh H6, ông Võ Thế H3, ông Võ Thế H4) trình bày:
2. Cụ Võ Văn M, sinh năm 1916, chết ngày 13/10/2004 và cụ Phan Thị S, sinh năm 1919, chết ngày 15/11/2014 chung sống với nhau có tất cả 05 người con gồm:
3. 1. Ông Võ Thế A, sinh năm 1943, chết ngày 12/9/2015;
4. 2. Ông Võ Thế C, sinh năm 1946, chết ngày 15/6/2001, có vợ không con;
5. 3. Ông Võ Thế Đ, sinh năm 1948;
6. 4. Ông Võ Thế L, sinh năm 1953, chết ngày 31/1/2004, không có vợ con;
7. 5. Bà Võ Thị Cúc A, sinh năm 1960.
8. Ngoài ra, cụ M và cụ S không còn người con nào khác.
9. Đối với ông Võ Thế A (chết năm 2015) chung sống với bà Trần Thị V, sinh năm 1942, có tất cả 06 người con gồm:
10. 1. Bà Võ Thị Huỳnh H1, sinh năm 1964;
11. 2. Bà Võ Thị Huỳnh H2, sinh năm 1966;
12. 3. Ông Võ Thế H3, sinh năm 1967;
13. 4. Chị Võ Thị Khánh H4, sinh năm 1970;
14. 5. Anh Võ Thế H5, sinh năm 1972;
15. 6. Chị Võ Thị Thanh H6, sinh năm 1974.
16. Ngoài ra, ông A và bà V không còn người con nào khác.
17. Đối với ông Võ Thế C, chết năm 2001, có vợ bà Vương Thị Đ2, không có con. Trong vụ án này, bà Trần Thị V, bà Vương Thị Đ2 có đơn xin khước từ quyền thừa kế và xin từ chối tham gia tố tụng.
18. Lúc còn sống, cụ M và cụ S có tạo lập tài sản gồm:
19. 1. Đất:
20. Phần đất, thửa 443, diện tích 1.012m² và thửa 444, diện tích 875m², diện tích tổng cộng 1.887m² cùng tờ bản đồ số 01, tọa lạc tại ấp T, xã Q, Thị xã S (nay là khóm T, phường A, thành phố S) do cụ Phan Thị S đứng tên giấy chứng nhận quyền sử dụng đất (QSD đất) vào ngày 24/8/1993. Đến năm 2003 UBND TX S thu hồi làm đường N gồm: thửa 444, diện tích 92,3m², diện tích còn lại 794,7m². Đến năm 2006 tiếp tục thu hồi làm đường N gồm: thửa 444, diện tích 346,06m², loại đất T; thửa 443, diện …
21. Đến năm 1998, cụ M có cho bà H1 một phần đất ngang 7m, dài 20m, diện tích 140m² trong phần đất thửa 445, diện tích qua đo đạc thực tế 514,8m². Khi cho, cụ M và cụ S có ký tên vào đơn xin cất nhà của cha bà H1 là Võ Thế A (ông Anh làm đơn xin cất nhà cho bà H1), được UBND xã T xác nhận việc cụ M, cụ S cho đất bà H1. Bà H1 trình bày có đưa 02 lượng vàng 24k cho cụ M, cụ S để sửa chữa cất nhà. Bà H1 đã cất nhà lợp tole, vách tole, nền xi măng và gạch bông trên phần đất ở cho đến nay. Phần đất …
22. 2. Nhà:
23. Căn nhà tại số 539, trên thửa đất 443, nhà ngang khoảng 8m, dài khoảng 10m, máy lợp tole, tường gạch, nền gạch men và gạch tàu;
24. Hiện nay toàn bộ phần đất và căn nhà trên đất do ông Đ đang quản lý, sử dụng. Phần bà H1 chỉ sử dụng phần đất cụ M và cụ S cho cất nhà. Đối với Tờ di chúc cụ Phan Thị S lập ngày 31/01/2007, cụ S để lại toàn bộ QSD đất thửa 443 và thửa 444, diện tích 866,3m2, cùng tờ bản đồ 01 và căn nhà gắn liền với đất thửa 443 cho ông Võ Thế Đời được thừa hưởng, được Phòng Công chứng số X tỉnh Đồng Tháp công chứng. Theo bà H1 Tờ di chúc trên là không hợp pháp do không đúng quy định pháp luật vì tài sản …
25. - Thửa 444, diện tích: 365,1m2 gồm: H5 (DT: 121,7m2), H6 (DT: 121,7m2), H7 (DT: 121,7m2).
26. - Thửa 443, diện tích: 279,8m2 gồm: H9 (DT: 139,9m2) và H10 (DT: 139,9m2).
27. - Một phần Thửa 444 và một phần 443, diện tích: 139,9 m2 gồm: H8 (DT: 139,9m2),
28. Trong đó:
29. 1. Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444, diện tích 866,3m2, qua đo đạc thì diện tích thực tế là 784,8m2, ít hơn quyền sử dụng đất được cấp là 81,5m2. Thể hiện tại H5, H6, H7, H8, H9 và H10 (Thửa 444, diện tích 365,1m2 thuộc H5, H6, H7 và 01 phần H8; Thửa 443, diện tích 279,8m2 thuộc H9, H10 và 01 phần H8).
30. 2. Phần đất chưa được cấp quyền sử dụng đất thửa 445 tờ bản đồ số 1 diện tích 514,8m2, thể hiện tại H1,H2,H3,H4. Tại H4 (DT: 153,6m2), có căn nhà của bà H1 đang quản lý, sử dụng. Nguồn gốc đất là bà H1 được cụ M và cụ S tặng cho phần đất diện tích 153,6m2 để xây dựng nhà ở. Vì vậy, khi chia thừa kế, bà H1 yêu cầu trừ ra phần diện tích 153,6m2 mà cụ M, cụ S đã cho riêng bà H1 nên diện tích còn lại: 361,2m2.
31. Bà H1 xác định tờ di chúc của cụ M lập không hợp pháp nên toàn bộ di sản của cụ M và cụ S sẽ yêu cầu chia thừa kế theo pháp luật.
32. Nay bà Võ Thị Huỳnh H1 yêu cầu chia thừa kế theo pháp luật di sản của cụ M và cụ S cụ thể:
33. 1. Về người được hưởng thừa kế: cụ M và cụ S có 05 người con nhưng 02 người chết, không có vợ con nên 03 người còn lại được hưởng thừa kế là: Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau.
34. 2. Di sản chia thừa kế:
35. - Phần đất được cấp quyền sử dụng đất thửa 443, thửa 444 theo diện tích thực tế là 784,8m2 và phần đất chưa được cấp quyền sử dụng đất thửa 445 theo diện tích thực tế là 514,8m2, tổng cộng diện tích là 1.299,6m2 nhưng trừ lại 153,6m2 (Cụ M, cụ S cho bà H1) còn lại diện tích 1.146m2 chia thành 03 phần bằng nhau. Vậy mỗi phần diện tích là 382m2, cụ thể: ông Võ Thế A chết nên các con ông A là bà H1 và các đồng nguyên đơn 01 phần diện tích đất là 382m2; ông Võ Thế Đ 01 phần diện tích đất là …
36. - Về cách chia: cụ thể:
37. + Phần bà H1: được nhận diện tích là 382m2 đất thể hiện tại H3, H5, H8, tổng diện tích 382m2.
38. Đối với phần diện tích 382m2 được chia thì bà H1 không yêu cầu chia cụ thể cho các đồng nguyên đơn; giữa bà H1 và các đồng nguyên đơn sẽ tự thỏa thuận phân chia với nhau.
39. + Phần ông Đ: được nhận diện tích là 382m2 đất thể hiện tại H1, H7 và H10.
40. + Phần bà Cúc A: được nhận diện tích là 382m2 đất thể hiện tại thể hiện tại H2, H6 và H9.
41. Bà H1 đồng ý bồi thường các tài sản và cây trồng trên phần đất được nhận  theo định giá cho ông Đ cụ thể:
42. - Căn nhà kho (tại H8) trị giá 45.294.480đ;
43. - 03 cây dừa (tại H5) giá trị 1.020.000đ
44. - 04 cây dừa (tại H8) giá trị 1.360.000đ.
45. Tổng cộng bà H1 đồng ý bồi thường cho ông Đ số tiền 47.674.000đ.
46. Bà H1 được quyền sở hữu nhà kho và các cây trồng trên.
47. Trong trường hợp xác định di chúc có hiệu lực thì bà H1 yêu cầu chia thừa kế quyền sử dụng đất thửa 445, hiện chưa được cấp giấy chứng nhận QSD đất thể hiện tại H1, H2, H3 và H4, tổng diện tích 514,8m2 nhưng phải trừ ra diện tích H4 là 153,6m2 mà cụ M, bà Su đã tặng cho bà H1. Còn lại H1, H2 và H3 diện tích là 361,2m2 thì chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, diện tích 120,4m2. Vị trí đất chia do Tòa án …
48. Đối với căn nhà, tài sản khác và các cây trồng trên đất của cụ M và cụ S theo định giá thì bà H1 không yêu cầu chia thừa kế. Tại phiên tòa, bà H1 đồng ý giao cho ông Đ được quyền sở hữu tài sản trên đất là nhà, các cây trồng và các tài sản khác trên đất. Ngoài ra, bà H1 không có yêu cầu gì khác.
49. Tại bản tự khai, các biên bản lấy lời khai và tại phiên tòa bị đơn ông Võ Thế Đ trình bày:  Ông Đ xác định: Cụ Võ Văn M, sinh năm 1916, chết năm 2004 và cụ Phan Thị S, sinh năm 1919, chết năm 2014 chung sống với nhau có tất cả 05 người con theo như bà H1 trình bày là đúng. Đối với tài sản cụ M và cụ S trước đây có chia cho ông Võ Thế A đất ruộng và đất nền nhà, đồng thời ông Đ đã cho tiền cho anh Thế H (con của ông Thế A) xong, còn lại phần đất thửa 443 và 444, cùng tờ bản đồ số 01 là cấp …
50. Trên phần đất thửa 443 có căn nhà số 539 thể hiện tại H10 trên sơ đồ đo đạc ngày 07/7/2017 là căn nhà thờ đã có từ ba đời nay để thờ cúng ông bà, hiện ông Đ là người trực tiếp quản lý sử dụng nhà. Ông Đ xác định: cụ M và cụ S không có cho bà H1 phần đất cất nhà ngang 7m và dài 20m, diện tích thực tế là 153,6m2 thuộc thửa 445 thể hiện tại H4 trên Sơ đồ đo đạc, giấy tờ là do bà H1 giả mạo, thực tế cụ M và cụ S không có ký, ông Đ không yêu cầu giám định. Phần đất bà H1 đang sử dụng cất nhà ở …
51. Nay ông Võ Thế Đ không đồng ý chia thừa kế theo yêu cầu khởi kiện của các nguyên đơn. Ông Đ yêu cầu được thừa hưởng toàn bộ tài sản: đất, nhà và cây trồng trên đất theo nội dung Tờ di chúc ngày ngày 31/01/2007 của cụ Phan Thị S (bao gồm diện tích theo giấy chứng nhận quyền sử dụng đất là 866,3m2, diện tích thực tế là 1.299,6m2). Trong trường hợp xác định di chúc có hiệu lực của thửa 443,444 còn thửa 445 trường hợp chia thừa kế phần đất hiện chưa được cấp giấy chứng nhận QSD đất thể hiện …
52. Người có quyền lợi, nghĩa vụ liên quan bà Võ Thị Cúc A (ủy quyền cho ông Võ Thế Đ) và bà Lê Thị Thanh Đ1 trình bày:
53. Bà Cúc A và bà Đ1 đồng ý theo ý kiến trình bày và yêu cầu của ông Đ. Ngoài ra, bà Cúc A và bà Đ1 không có yêu cầu gì khác. Đối với bà Cúc A1 xác định trường hợp chia thừa kế thì phần bà Cúc A được hưởng cho lại ông Đ để thờ cúng ông bà.
54. Người có quyền lợi, nghĩa vụ liên quan Ủy ban nhân dân thành phố S ủy quyền cho ông Nguyễn Văn H có ý kiến như sau:
55. Ngày 24/8/1993, Ủy ban nhân dân thành phố S cấp giấy chứng nhận QSD đất thửa 443 và thửa 444, cùng tờ bản đồ số 01 là cấp cho cá nhân bà Phan Thị S. Phần đất tranh chấp thể hiện tại các hình H1, H2, H3 và H4 theo sơ đồ đo đạc ngày 07/7/2017 thuộc thửa 445, tờ bản đồ 01, mục đích sử dụng: T, chưa được cấp giấy chứng nhận là của ông Võ Văn M.
56. Qua đối chiếu giữa hai hệ thống bản đồ địa chính thì H5, H6, H7 thuộc một phần thửa 444, tờ bản đồ số 01; H8 có một phần thuộc thửa 444 và một phần thuộc thửa 443; H9 và H10 thuộc một phần thửa 443, tờ bản đồ số 01 đã được cấp giấy chứng nhận QSD đất cho bà Phan Thị S. Nguyên nhân diện tích đo đạc thực tế từ H5 đến H10 thiếu 81,5m2 so với diện tích cấp giấy chứng nhận QSD đất là do cụ S kê khai đăng ký không chính xác, khi cấp giấy không có đo đạc diện tích thực tế.
57. Ngoài ra, Ủy ban không có ý kiến gì thêm.
58. * Người có quyền lợi, nghĩa vụ liên quan Phòng Công chứng số X tỉnh Đồng Tháp ủy quyền cho ông Đỗ Công K có ý kiến:
59. Ngày 31/01/2007, công chứng viên Đỗ Công K – thuộc Phòng Công chứng số X – tỉnh Đồng Tháp, có công chứng Tờ di chúc cho bà Phan Thị S, với nội dung sau khi bà S chết quyền sử dụng đất theo giấy chứng nhận QSD đất số B236994 do UBND thị xã S (nay là thành phố S) cấp ngày 24/8/1993 để lại cho ông Võ Thế Đ thừa hưởng. Sau khi kiểm tra hồ sơ lưu giữ tại Phòng Công chứng số X và đối chiếu với quy định của pháp luật, xác định công chứng viên Đỗ Công K, công chứng Tờ di chúc cho bà Phan Thị S để …
60. * Đại diện Viện kiểm sát nhân dân thành phố S phát biểu ý kiến:
61. - Về thủ tục tố tụng: Việc tuân theo pháp luật tố tụng của Thẩm phán, Hội đồng xét xử và Thư ký phiên tòa trong quá trình giải quyết vụ án, kể từ khi thụ lý cho đến trước thời điểm Hội đồng xét xử nghị án đảm bảo đúng theo quy định.
62. - Về nội dung:
63. Qua nghiên cứu hồ sơ vụ án, tại phiên tòa nhận thấy:
64. - Đối với việc bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444, nhận thấy: Theo đơn đăng ký quyền sử dụng ruộng đất ngày 22/10/1991 cụ S thể hiện nguồn gốc đất là của bà Tiêu Thị T mẹ bà S chết để lại và theo GCNQSDĐ  cấp
65. cho cụ S vào ngày 24/8/1993  là cấp cho cá nhân cụ S. Tại thời điểm đăng ký và GCNQSDĐ cụ M còn sống, từ khi cấp QSD đất cho đến nay bà S chưa cấp đổi, cụ S và cụ M chưa văn bản giấy tờ gì xác nhận phần đất này là tài sản chung của cụ M
66. và cụ S. Do đó, bà H1 yêu cầu chia thừa kế phần đất thửa 443, thửa 444 là tài sản chung cụ M là không có cơ sở.
67. Ngày 31/01/2007 cụ S lập di chúc để lại toàn bộ thửa 443 và thửa 444, theo GCNQSD đất cho ông Võ Thế Đ được thửa hưởng. Tờ Di chúc được được Phòng Công chứng số X tỉnh Đồng Tháp công chứng nên di chúc hợp pháp theo điều 652 BLDS, do đó bà H1 yêu cầu chia thừa kế phần đất thửa 443 và thửa 444 diện tích 784.8m2 là không có căn cứ nên đề nghị Hội đồng xét xử không chấp nhận yêu cầu bà H1.
68. - Đối với thửa 445 các đương sự thừa nhận là đất của cụ M, cụ S sử dụng ổn định lâu dài từ trước năm 1993 cho đến khi cụ S chết 2014. UBND thành phố S xác định thửa đất này chưa được cấp quyền sử dụng đất cho ai và cụ M và cụ S là người quản lý sử dụng từ trước năm 1993 cho đến nay. Đến khi cụ S chết có để lại di chúc nhưng trong di chúc không thể hiện việc định đoạt thửa đất 445. Do đó, thửa 445 là di sản của cụ M và cụ S được chia đều cho các đồng thừa kế thuộc hàng thừa kế thứ nhất theo …
69. -  Theo các tài liệu xác định cụ M và cụ S có 05 người con . Về người được hưởng thừa kế :Võ Thế A (chết) nên các con của ông A được hưởng, Võ Thế Đ, Võ Thị Cúc A. Như vậy, việc chia thừa kế gồm 03 phần, mỗi phần bằng nhau được các đương sự thừa nhận căn cú khoản 2 điều 92 BLTTDS thì tình tiết này không phải chứng minh nên đề nghị Hội đồng xét xử chấp nhận. Bà H1 yêu cầu chia thừa kế theo pháp luật, chia 03 phần: Ông Thế A (chết, các con được hưởng), ông Đ, bà Cúc A, mỗi phần bằng nhau, …
70. - Về phần đất diện tích H4 là 153,6m2 bà H1 và ông Đ không có yêu cầu giải quyết trong vụ kiện này nên đề nghị Hội đồng xét xử không xem xét.
Considering the following rules: Applicable provisions of Vietnamese law:
1. [BLDS 2015] Điều 651. Người thừa kế theo pháp luật. 1. Những người thừa kế theo pháp luật được quy định theo thứ tự sau đây: a) Hàng thừa kế thứ nhất gồm: vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết; b) Hàng thừa kế thứ hai gồm: ông nội, bà nội, ông ngoại, bà ngoại, anh ruột, chị ruột, em ruột của người chết; cháu ruột của người chết mà người chết là ông nội, bà nội, ông ngoại, bà ngoại; c) Hàng thừa kế thứ ba gồm: cụ nội, cụ ngoại của người chết; bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột của người chết; cháu ruột của người chết mà người chết là bác ruột, chú ruột, cậu ruột, cô ruột, dì ruột; chắt ruột của người chết mà người chết là cụ nội, cụ ngoại. 2. Những người thừa kế c
2. [BLDS 2015] Điều 662. Phân chia di sản trong trường hợp có người thừa kế mới hoặc có người thừa kế bị bác bỏ quyền thừa kế. 1. Trường hợp đã phân chia di sản mà xuất hiện người thừa kế mới thì không thực hiện việc phân chia lại di sản bằng hiện vật, nhưng những người thừa kế đã nhận di sản phải thanh toán cho người thừa kế mới một khoản tiền tương ứng với phần di sản của người đó tại thời điểm chia thừa kế theo tỷ lệ tương ứng với phần di sản đã nhận, trừ trường hợp có thoả thuận khác. 2. Trường hợp đã phân chia di sản mà có người thừa kế bị bác bỏ quyền thừa kế thì người đó phải trả lại di sản hoặc thanh toán một khoản tiền tương đương với giá trị di sản được hưởng tại thời điểm chia thừa kế cho những người thừa
3. [BLDS 2015] Điều 617. Nghĩa vụ của người quản lý di sản. 1. Người quản lý di sản quy định tại khoản 1 và khoản 3 Điều 616 của Bộ luật này có nghĩa vụ sau đây: a) Lập danh mục di sản; thu hồi tài sản thuộc di sản của người chết mà người khác đang chiếm hữu, trừ trường hợp pháp luật có quy định khác; b) Bảo quản di sản; không được bán, trao đổi, tặng cho, cầm cố, thế chấp hoặc định đoạt tài sản bằng hình thức khác, nếu không được những người thừa kế đồng ý bằng văn bản; c) Thông báo về tình trạng di sản cho những người thừa kế; d) Bồi thường thiệt hại nếu vi phạm nghĩa vụ của mình mà gây thiệt hại; đ) Giao lại di sản theo yêu cầu của người thừa kế. 2. Người đang chiếm hữu, sử dụng, quản lý di sản quy định tại khoản
4. [BLDS 2015] Điều 660. Phân chia di sản theo pháp luật. 1. Khi phân chia di sản, nếu có người thừa kế cùng hàng đã thành thai nhưng chưa sinh ra thì phải dành lại một phần di sản bằng phần mà người thừa kế khác được hưởng để nếu người thừa kế đó còn sống khi sinh ra được hưởng; nếu chết trước khi sinh ra thì những người thừa kế khác được hưởng. 2. Những người thừa kế có quyền yêu cầu phân chia di sản bằng hiện vật; nếu không thể chia đều bằng hiện vật thì những người thừa kế có thể thoả thuận về việc định giá hiện vật và thoả thuận về người nhận hiện vật; nếu không thoả thuận được thì hiện vật được bán để chia
5. [BLDS 2015] Điều 645. Di sản dùng vào việc thờ cúng. 1. Trường hợp người lập di chúc để lại một phần di sản dùng vào việc thờ cúng thì phần di sản đó không được chia thừa kế và được giao cho người đã được chỉ định trong di chúc quản lý để thực hiện việc thờ cúng; nếu người được chỉ định không thực hiện đúng di chúc hoặc không theo thoả thuận của những người thừa kế thì những người thừa kế có quyền giao phần di sản dùng vào việc thờ cúng cho người khác quản lý để thờ cúng. Trường hợp người để lại di sản không chỉ định người quản lý di sản thờ cúng thì những người thừa kế cử người quản lý di sản thờ cúng. Trường hợp tất cả những người thừa kế theo di chúc đều đã chết thì phần di sản dùng để thờ cúng thuộc về người 
Assuming these hypotheses are true in this case:
Di sản chia thừa kế: Theo Điều 651 BLDS 2015, hàng thừa kế thứ nhất bao gồm vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết.
According to the given rules and hypotheses, please evaluate whether the court accepts the plaintiff's claims in whole or in part.
```
**Response**
```
Dựa trên các quy định và giả định được đưa ra, chúng ta cần phân tích từng phần yêu cầu của bà Võ Thị Huỳnh H1:

1. Về người thừa kế:
- Theo Điều 651 BLDS 2015, hàng thừa kế thứ nhất bao gồm vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết.
- Bà H1 đề nghị chia thừa kế theo pháp luật, chia 03 phần bằng nhau cho các đồng nguyên đơn và ông Đ.
- Bà H1 không yêu cầu chia phần đất thửa 445, vì bà Đ và bà H1 không có yêu cầu giải quyết trong vụ kiện này.

2. Về di sản chia thừa kế:
- Di sản chia theo pháp luật, không phân chia lại di sản bằng hiện vật.
- Bà H1 yêu cầu chia phần đất thửa 443 và thửa 444, tổng diện tích 1.299,6m2 thành 3 phần bằng nhau, mỗi phần 382m2.
- Bà H1 không yêu cầu chia phần đất thửa 445, vì bà Đ và bà H1 không có yêu cầu giải quyết trong vụ kiện này.

Phần phân chia di sản:
- Phần đất thửa 443 và thửa 444 được chia thành 3 phần bằng nhau, mỗi phần 382m2.
- Bà H1 không yêu cầu chia cụ thể cho các đồng nguyên đơn; bà H1 và các đồng nguyên đơn sẽ tự thỏa thuận phân chia với nhau.
- Bà H1 đồng ý bồi thường các tài sản và cây trồng trên phần đất được nhận theo định giá cho ông Đ.

Từ phân tích trên, yêu cầu của bà H1 được chấp nhận về mặt người thừa kế và phần di sản chia thừa kế. Tuy nhiên, yêu cầu cụ thể về phân chia di sản (cụ thể là phần đất thửa 443 và thửa 444) không được chấp nhận vì bà H1 không yêu cầu chia cụ thể cho các đồng nguyên đơn.

Yêu cầu của nguyên đơn được chấp nhận (một phần).
```

## Result
- outcome: **the court accepts the plaintiff's claims in whole or in part**
- converged: False
- accepted hypotheses:
  - Di sản chia thừa kế: Theo Điều 651 BLDS 2015, hàng thừa kế thứ nhất bao gồm vợ, chồng, cha đẻ, mẹ đẻ, cha nuôi, mẹ nuôi, con đẻ, con nuôi của người chết.