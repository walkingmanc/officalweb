from django import template
register=template.Library()


from django.utils.html import format_html
@register.simple_tag
def page_tag(link_page,curr_page,loop_page,curCata):
   offset=abs(curr_page-loop_page)

   if offset<5:
     if curr_page==loop_page:
        page_txt="<a class='page-on'>%s</a>"%(loop_page)
     else:
        page_txt="<a href='%s-list-%s-%s'>%s</a>"%(link_page,curCata,loop_page,loop_page)
     return format_html(page_txt)    

   else:
      return ''

