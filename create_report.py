import markdown
import pdfkit

Chat_database = ['1. #Online Cooking Class# $Culinary Instructor$ - |Identify and define your target audience in Germany. Create a business plan that outlines your mission, offerings, and pricing structure. Develop a website and use social media platforms to promote your online cooking classes. Make sure to build a professional kitchen setup for your video content. Invest in high-quality video and audio equipment to ensure your classes are easy to follow|\n\n2. #E-commerce Kitchen Tools Store# $E-commerce expert$ - |Conduct market research to determine which kitchen tools are in demand in Germany. Look for reliable suppliers of these products. Create an user-friendly e-commerce website that offers secure transactions. Invest in marketing initiatives to increase your customer base. Provide excellent customer service to retain your existing customers|\n\n3. #Food Delivery Service Provider# $Logistics and Planning Expert$ - |Identify densely populated locations in Germany where demand for food delivery services is high. Create partnerships with restaurants in these areas. Invest in an efficient dispatch system. Hire reliable drivers and make sure they have thorough knowledge of the delivery areas. Promote your service through online and offline marketing strategies like social media, local newsletters, and flyers|.\n', {'num': '1', 'title': 'Online Cooking Class', 'expert': 'Culinary Instructor', 'content': 'Identify and define your target audience in Germany. Create a business plan that outlines your mission, offerings, and pricing structure. Develop a website and use social media platforms to promote your online cooking classes. Make sure to build a professional kitchen setup for your video content. Invest in high-quality video and audio equipment to ensure your classes are easy to follow', 'prompt': 'You are the best Culinary Instructor in the whole world, with 20 years experience. I am your client and i want to start Online Cooking Class in the Germany. Describe in detail and write what is needed to start. No need to mention the current year(2021) in the answer. Write strictly in the format: number. #name of the idea# $the area expert$ - |business action in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion', 'elaborate': ['1. #Niche Identification# $Market Research Expert$ - |Identify your target audience. Understand their demographics, their preferences, their cooking skill levels. Ensure your business idea is tailored to the needs and preferences of your target customers|\n\n2. #Curriculum Development# $Culinary Instructor$ - |Draw on your culinary experience to develop a curriculum for your online cooking class. Consider the skill level of your target audience. Your classes could range from basic techniques for beginners, to more specialized or regional cuisines for more advanced students|\n\n3. #Equipment and Technology# $Online Learning Specialist$ - |Invest in high quality cooking equipment and camera setup to demonstrate your recipes in the clearest possible way. Use a stable and user-friendly platform to host your online classes, such as Zoom, Skype, Google Meet|\n\n4. #Website Development and Marketing# $Digital Marketing Expert$ - |Build a professional, easy-to-navigate website for potential students to find information about your classes, book their places and make payments. Use Search Engine Optimization (SEO) to ensure your website is easily discoverable. Leverage social media platforms to promote your online cooking classes and engage with your audience|\n\n5. #Customer Experience# $Business Operations Expert$ - |Develop systems for accepting payments, scheduling classes, sending class materials and providing customer support. Ensure that all of these processes are efficient and user-friendly in order to provide a positive customer experience|\n\n6. #Legalities and Regulations# $Business Law Specialist$ - |Ensure you meet all legal requirements for starting an online business in Germany, including registering your business and understanding tax obligations|.', {'num': '1', 'title': 'Niche Identification', 'expert': 'Market Research Expert', 'content': 'Identify your target audience. Understand their demographics, their preferences, their cooking skill levels. Ensure your business idea is tailored to the needs and preferences of your target customers'}, {'num': '2', 'title': 'Curriculum Development', 'expert': 'Culinary Instructor', 'content': 'Draw on your culinary experience to develop a curriculum for your online cooking class. Consider the skill level of your target audience. Your classes could range from basic techniques for beginners, to more specialized or regional cuisines for more advanced students', 'prompt': "Your current choice of business action is Curriculum Development. Imagine it's September 2021. you're the best Culinary Instructor in the whole world, with 20 years of experience. I'm your client and i want you to fetch me a detailed report corresponding to this business action using the following information.\n Draw on your culinary experience to develop a curriculum for your online cooking class. Consider the skill level of your target audience. Your classes could range from basic techniques for beginners, to more specialized or regional cuisines for more advanced students \nNo need to mention the current year in the answer.\nWrite strictly in the format: number. #name of the idea# $the area expert$ - |business action in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion", 'elaborate': ["1. #Identifying Skill Levels# $Educational Consultant$ - |Define the skill levels of your potential students, this could be beginners, intermediate, or advanced. This will help in creating a course outline that caters to all individuals|\n\n2. #Structured Course Development# $Curriculum Expert$ - |For beginners, start with basics like knife skills, cooking techniques, hygiene & safety, meal planning and prep. Intermediate courses can include in-depth techniques like pastry making, sauces, and advanced cooking techniques. Advanced classes can delve into specialized and regional cuisines of Germany, including but not limited to Swabian, Franconian and Bavarian|\n\n3. #Interactive Content Creation# $Instructional Design Expert$ - |Develop interactive and engaging content. This could include video demonstrations, quizzes, discussion boards, amongst others. Ensure the content is easy to follow and can efficiently be used for self-study|\n\n4. #Course Materials# $Educational Resource Specialist$ - |Prepare necessary course materials like recipes, videos, articles, quizzes, etc. These may also include optional reading lists for further study|\n\n5. #Feedback and Evaluation# $Educational Assessor$ - |Develop a feedback system. This could be quizzes or assignments at the end of each module. Assess student's progress and provide them constructive feedback. This will help them get an understanding of their learning progress and areas they need to work on|.", {'num': '1', 'title': 'Identifying Skill Levels', 'expert': 'Educational Consultant', 'content': 'Define the skill levels of your potential students, this could be beginners, intermediate, or advanced. This will help in creating a course outline that caters to all individuals'}, {'num': '2', 'title': 'Structured Course Development', 'expert': 'Curriculum Expert', 'content': 'For beginners, start with basics like knife skills, cooking techniques, hygiene & safety, meal planning and prep. Intermediate courses can include in-depth techniques like pastry making, sauces, and advanced cooking techniques. Advanced classes can delve into specialized and regional cuisines of Germany, including but not limited to Swabian, Franconian and Bavarian'}, {'num': '3', 'title': 'Interactive Content Creation', 'expert': 'Instructional Design Expert', 'content': 'Develop interactive and engaging content. This could include video demonstrations, quizzes, discussion boards, amongst others. Ensure the content is easy to follow and can efficiently be used for self-study'}, {'num': '4', 'title': 'Course Materials', 'expert': 'Educational Resource Specialist', 'content': 'Prepare necessary course materials like recipes, videos, articles, quizzes, etc. These may also include optional reading lists for further study'}, {'num': '5', 'title': 'Feedback and Evaluation', 'expert': 'Educational Assessor', 'content': "Develop a feedback system. This could be quizzes or assignments at the end of each module. Assess student's progress and provide them constructive feedback. This will help them get an understanding of their learning progress and areas they need to work on"}]}, {'num': '3', 'title': 'Equipment and Technology', 'expert': 'Online Learning Specialist', 'content': 'Invest in high quality cooking equipment and camera setup to demonstrate your recipes in the clearest possible way. Use a stable and user-friendly platform to host your online classes, such as Zoom, Skype, Google Meet'}, {'num': '4', 'title': 'Website Development and Marketing', 'expert': 'Digital Marketing Expert', 'content': 'Build a professional, easy-to-navigate website for potential students to find information about your classes, book their places and make payments. Use Search Engine Optimization (SEO) to ensure your website is easily discoverable. Leverage social media platforms to promote your online cooking classes and engage with your audience'}, {'num': '5', 'title': 'Customer Experience', 'expert': 'Business Operations Expert', 'content': 'Develop systems for accepting payments, scheduling classes, sending class materials and providing customer support. Ensure that all of these processes are efficient and user-friendly in order to provide a positive customer experience'}, {'num': '6', 'title': 'Legalities and Regulations', 'expert': 'Business Law Specialist', 'content': 'Ensure you meet all legal requirements for starting an online business in Germany, including registering your business and understanding tax obligations'}]}, {'num': '2', 'title': 'E-commerce Kitchen Tools Store', 'expert': 'E-commerce expert', 'content': 'Conduct market research to determine which kitchen tools are in demand in Germany. Look for reliable suppliers of these products. Create an user-friendly e-commerce website that offers secure transactions. Invest in marketing initiatives to increase your customer base. Provide excellent customer service to retain your existing customers', 'prompt': 'You are the best E-commerce expert in the whole world, with 20 years experience. I am your client and i want to start E-commerce Kitchen Tools Store in the Germany. Describe in detail and write what is needed to start. No need to mention the current year(2021) in the answer. Write strictly in the format: number. #name of the idea# $the area expert$ - |business action in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion', 'elaborate': ['1. #Market Research# $E-commerce expert$ - |Identify your competitors and analyze their strategies. Understand your target audience, their preferences, and what they value in kitchen tools. Discover the best-selling and most preferred brands. Gather insights about the price range customers are willing to pay|\n\n2. #E-commerce Platform# $Web Development Expert$ - |Start by choosing a reliable e-commerce platform that suits your business requirements. Customize your website design, ensuring it is user-friendly. Make sure your site supports multiple payments and language options. Invest in search engine optimization for better visibility|\n\n3. #Product Acquisition# $Inventory Management Expert$ - |Source your kitchen tools from reliable manufacturers or wholesalers. Prioritize quality to build trust with your customers. Also ensure your supplier can maintain a consistent stock according to your demand|\n\n4. #Warehousing and Logistics# $Supply Chain Expert$ - |Organize a secure and efficient warehouse operation for storing your products. Set up a reliable system for inventory management. Pair up with a trustworthy logistics provider to ensure prompt and secure delivery of orders|\n\n5. #Marketing and Customer Service# $Digital Marketing Expert$ - |Develop an effective marketing plan to reach your targeted audience, this can include SEO, social media promotions and email marketing. Invest in creating attractive product photos and descriptions. Establish excellent customer service to handle inquiries, returns or any issues customers may encounter.|\n', {'num': '1', 'title': 'Market Research', 'expert': 'E-commerce expert', 'content': 'Identify your competitors and analyze their strategies. Understand your target audience, their preferences, and what they value in kitchen tools. Discover the best-selling and most preferred brands. Gather insights about the price range customers are willing to pay'}, {'num': '2', 'title': 'E-commerce Platform', 'expert': 'Web Development Expert', 'content': 'Start by choosing a reliable e-commerce platform that suits your business requirements. Customize your website design, ensuring it is user-friendly. Make sure your site supports multiple payments and language options. Invest in search engine optimization for better visibility'}, {'num': '3', 'title': 'Product Acquisition', 'expert': 'Inventory Management Expert', 'content': 'Source your kitchen tools from reliable manufacturers or wholesalers. Prioritize quality to build trust with your customers. Also ensure your supplier can maintain a consistent stock according to your demand', 'prompt': "Your current choice of business action is Product Acquisition. Imagine it's September 2021. you're the best Inventory Management Expert in the whole world, with 20 years of experience. I'm your client and i want you to fetch me a detailed report corresponding to this business action using the following information.\n Source your kitchen tools from reliable manufacturers or wholesalers. Prioritize quality to build trust with your customers. Also ensure your supplier can maintain a consistent stock according to your demand \nNo need to mention the current year in the answer.\nWrite strictly in the format: number. #name of the idea# $the area expert$ - |business action in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion", 'elaborate': ['1. #Supplier Identification# $Sourcing Expert$ - |Research and identify potential manufacturers or wholesalers of kitchen tools both locally and internationally. Look for their reputation, quality of products, and track record. Initiate discussions and obtain product samples before finalizing|\n\n2. #Product Quality Assessment# $Quality Assurance Expert$ - |Prioritize quality over everything else. Evaluate the samples on various parameters like durability, functionality and aesthetic appeal. Reiterate with the supplier on your quality expectations|\n\n3. #Order Management# $Inventory Management Expert$ - |Based on your market research, forecast the demand for different products. Place a relatively smaller order to begin with, observe the response and adapt accordingly. Ensure that the supplier can meet your restock requirements on time|\n\n4. #Supplier Relationship Management# $Relationship Management Expert$ - |Establish clear terms and conditions with your supplier including cost, delivery time and returns on defective items. Ensure prompt payments and good communication with your supplier to build a long-term relationship|.\n', {'num': '1', 'title': 'Supplier Identification', 'expert': 'Sourcing Expert', 'content': 'Research and identify potential manufacturers or wholesalers of kitchen tools both locally and internationally. Look for their reputation, quality of products, and track record. Initiate discussions and obtain product samples before finalizing', 'prompt': "Your current choice of business action is Supplier Identification. Imagine it's September 2021. you're the best Sourcing Expert in the whole world, with 20 years of experience. I'm your client and i want you to fetch me a detailed report corresponding to this business action using the following information.\n Research and identify potential manufacturers or wholesalers of kitchen tools both locally and internationally. Look for their reputation, quality of products, and track record. Initiate discussions and obtain product samples before finalizing \nNo need to mention the current year in the answer.\nWrite strictly in the format: number. #name of the idea# $the area expert$ - |business action in imperative form for the second person| Use only these seperators:#$| do not write an introduction or a conclusion", 'elaborate': ['1. #Desk Research# $Sourcing Expert$ - |Conduct a thorough online research on potential manufacturers and wholesalers of kitchen tools. Use sourcing platforms like Alibaba or Global sources. Consider local trade directories and chambers of commerce as good sources of information|\n\n2. #Reputation and Quality Assessment# $Quality Control Expert$ - |Look for reviews and ratings of the suppliers identified. Check their accreditation and certifications, if any, from recognized institutions. Get in touch with their previous or existing clients to gather unbiased feedback|\n\n3. #Sample Testing# $Product Testing Expert$ - |Request samples from the suppliers. Evaluate them against criteria such as quality, durability, and usability. Involve a third-party inspection agency if required, to ensure unbiased assessment|\n\n4. #Supplier Communication# $Negotiation Expert$ - |Initiate conversations with the shortlisted suppliers. Discuss your requirements, order quantities, pricing, and delivery timelines. Try to negotiate on the terms of supply, keeping in mind to build a win-win relationship|.\n', {'num': '1', 'title': 'Desk Research', 'expert': 'Sourcing Expert', 'content': 'Conduct a thorough online research on potential manufacturers and wholesalers of kitchen tools. Use sourcing platforms like Alibaba or Global sources. Consider local trade directories and chambers of commerce as good sources of information'}, {'num': '2', 'title': 'Reputation and Quality Assessment', 'expert': 'Quality Control Expert', 'content': 'Look for reviews and ratings of the suppliers identified. Check their accreditation and certifications, if any, from recognized institutions. Get in touch with their previous or existing clients to gather unbiased feedback'}, {'num': '3', 'title': 'Sample Testing', 'expert': 'Product Testing Expert', 'content': 'Request samples from the suppliers. Evaluate them against criteria such as quality, durability, and usability. Involve a third-party inspection agency if required, to ensure unbiased assessment'}, {'num': '4', 'title': 'Supplier Communication', 'expert': 'Negotiation Expert', 'content': 'Initiate conversations with the shortlisted suppliers. Discuss your requirements, order quantities, pricing, and delivery timelines. Try to negotiate on the terms of supply, keeping in mind to build a win-win relationship|.'}]}, {'num': '2', 'title': 'Product Quality Assessment', 'expert': 'Quality Assurance Expert', 'content': 'Prioritize quality over everything else. Evaluate the samples on various parameters like durability, functionality and aesthetic appeal. Reiterate with the supplier on your quality expectations'}, {'num': '3', 'title': 'Order Management', 'expert': 'Inventory Management Expert', 'content': 'Based on your market research, forecast the demand for different products. Place a relatively smaller order to begin with, observe the response and adapt accordingly. Ensure that the supplier can meet your restock requirements on time'}, {'num': '4', 'title': 'Supplier Relationship Management', 'expert': 'Relationship Management Expert', 'content': 'Establish clear terms and conditions with your supplier including cost, delivery time and returns on defective items. Ensure prompt payments and good communication with your supplier to build a long-term relationship|.'}]}, {'num': '4', 'title': 'Warehousing and Logistics', 'expert': 'Supply Chain Expert', 'content': 'Organize a secure and efficient warehouse operation for storing your products. Set up a reliable system for inventory management. Pair up with a trustworthy logistics provider to ensure prompt and secure delivery of orders'}, {'num': '5', 'title': 'Marketing and Customer Service', 'expert': 'Digital Marketing Expert', 'content': 'Develop an effective marketing plan to reach your targeted audience, this can include SEO, social media promotions and email marketing. Invest in creating attractive product photos and descriptions. Establish excellent customer service to handle inquiries, returns or any issues customers may encounter.'}]}, {'num': '3', 'title': 'Food Delivery Service Provider', 'expert': 'Logistics and Planning Expert', 'content': 'Identify densely populated locations in Germany where demand for food delivery services is high. Create partnerships with restaurants in these areas. Invest in an efficient dispatch system. Hire reliable drivers and make sure they have thorough knowledge of the delivery areas. Promote your service through online and offline marketing strategies like social media, local newsletters, and flyers|.'}]




def create_report_as_md_file(Chat_database, businessplan):
    with open(businessplan,'w', encoding = 'utf-8') as md_file:
        for i in [1,2,3]:
            data= Chat_database[i]
            if 'elaborate' in data:

                md_file.write(f"# Idea_{i}: {data['title']}\n\n")
                md_file.write(f"{data['content']}\n\n")
            
                dict_list1 = [item for item in data['elaborate'] if isinstance(item,dict)]
                md_file.write(f"**Business Action Plans:**\n\n")
                for item in dict_list1:
                    md_file.write(f"{item['num']}. **{item['title']}:**\n")
                    md_file.write(f"    * {item['content']}\n")
                    md_file.write("\n")
                
                    if 'elaborate' in item:
                        dict_list2 = [subitem for subitem in item['elaborate'] if isinstance(subitem,dict)]
                        md_file.write(f"    **Business Action Elaborations:**\n\n")
                        for subitem in dict_list2:
                            md_file.write(f"    {subitem['num']}. **{subitem['title']}:**\n")
                            md_file.write(f"        - {subitem['content']}\n")
                            md_file.write("\n")
                        
                            if 'elaborate' in subitem:
                                dict_list3 = [subitem1 for subitem1 in subitem['elaborate'] if isinstance(subitem1,dict)]
                                for subitem1 in dict_list3:
                                    md_file.write(f"        {subitem1['num']}. **{subitem1['title']}:**\n")
                                    md_file.write(f"            - {subitem1['content']}\n\n")
                                    md_file.write("\n")

                                    if 'elaborate' in subitem1:
                                        dict_list4 = [subitem2 for subitem2 in subitem1['elaborate'] if isinstance(subitem2,dict)]
                                        for subitem2 in dict_list4:
                                            md_file.write(f"            {subitem2['num']}. **{subitem2['title']}:**\n")
                                            md_file.write(f"                - {subitem2['content']}\n")
                                            md_file.write("\n")




create_report_as_md_file(Chat_database, 'businessplan.md')

def md_to_pdf(md_content, output_file):
    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)
    
    # Convert HTML to PDF
    pdfkit.from_string(html_content, output_file)

with open("businessplan.md", "r") as file:
    md_content = file.read()
md_to_pdf(md_content, "businessplan.pdf")