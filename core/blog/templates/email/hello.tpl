{%extends 'mail_templated/base.tpl'%}

{%block subject%}
Hello {{name}}
{%endblock%}

{%block html%}
This is an email <strong>test</strong>
{%endblock%}