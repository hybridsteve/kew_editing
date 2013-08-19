from django.http import HttpResponse
from django.template import RequestContext, loader

from front.models import ProjectType, Project

# Begins html document, defines common header tags.
def begin_html(title):
	html = """
	<!DOCTYPE html>
	<html lang='eng'>
		<head>
			<meta charset='utf-8'>
			<title>Kristen Ebert-Wagner Editing: %s</title>
			<link rel='stylesheet' type='text/css' href='/static/inengmaj.css' />
		</head>
		<body>""" % (title)
	return html

# Ends html document.
def close_html():
	html = "</body></html>"
	return html

# Begins body, defines header and navigation.
def common_header():
	html = """
		<div class='page-header'>
			<span class='editor'>Kristen Ebert-Wagner</span>
			<span class='service'>editing &amp; writing</span> /
			<span class='telephone'>607.591.0048</span>
		</div>
		<div class='navigation header-navigation'>
			<ul>
				<li><strong><a href='/home'>home</a></strong></li>
				<li><strong><a href='/services'>services</a></strong></li>
				<li><strong><a href='/clients'>clients</a></strong></li>
				<li><strong><a href='/details'>details</a></strong></li>
				<li><strong><a href='/faq'>FAQ</a></strong></li>
			</ul>
		</div>"""
	return html

# Ends body, defines footer.
def common_footer():
	html = """
		<div class='footer'>
			<div class='navigation footer-navigation'>
				<ul>
					<li><a href='https://www.onlinefilefolder.com'><strong>log in to secure file transfer area</strong></a><br/>
						<a href='securelogin'>(what's this?)</a></li>
					<li><a href='/paypal'><strong>pay invoice</strong><br/>
						with PayPal</a></li>
					<li><a href='/contactindex'><strong>request an estimate/<br/>contact me</strong></a></li>
				</ul>
			</div>
			<p>personal checks, credit cards, and university purchase orders accepted<br/><strong>international faculty and students welcome</strong></p>
			<p class='copyright'>copyright &copy; 2003-2013 <span class='maroon-text'>~</span> Kristen Ebert-Wagner</p>
		</div>
		<script type='text/javascript' href='/static/jquery.js'></script>
		<script type='text/javascript' href='/static/inengmaj.js'></script>"""
	return html

# Given content html string, puts all the parts of a page together and returns the complete HttpResponse.
def view_constructor(content, title):
	html = begin_html(title)
	html += common_header() + content + common_footer()
	html += close_html()
	return HttpResponse(html)

def home(request):
	content = "<h1>home view</h1>"
	return view_constructor(content, "Home")

def services(request):
	content = """
		<div class='content inner-padding'>
			<h6>substantive editing and copyediting of nonfiction manuscripts</h6><p>manuscript preparation</p>
			<p>editing for punctuation, grammar, and usage; clarity, concision, and consistency; logical flow; and adherence to university or publisher requirements
				</p>
			<p>formatting for citations, references, and copyediting to ensure adherence to style manual specifications: 
				</p>
			<p><em>American Psychological Association [APA] 5th and 6th editions<br/>
				Chicago Manual of Style 15th and 16th editions<br/>
				other journal style guidelines</em>
				</p>
			<h6>journal article editing and formatting</h6>
			<p>ensuring that articles meet journal style requirements</p>
			<h6>dissertation and thesis formatting</h6>
			<p>specializing in document formatting for electronic filing with the Cornell Graduate School&mdash;from title page to bibliography</p>
			<h6>EndNote wrangling</h6>
			<p>taming EndNote libraries</p>
		</div>
	"""
	return view_constructor(content, "Services")

def clients(request):
	content = """
		<div class='content inner-padding'>
			<p><strong class='maroon-text'>some recent clients and their projects</strong></p>
			<h6>copyediting: books</h6>
			<h6>editing: dissertation and theses (formatting included)</h6>
			<h6>formatting: dissertations and theses</h6>
			<h6>journal articles</h6>
		</div>
	"""
	project_types = ProjectType.objects.order_by('id')
	projects = Project.objects.order_by('pub_date')
	template = loader.get_template('front/projects.html')
	context = RequestContext(request, {
		"project_types": project_types,
		"projects": projects
	})
	templated_content = template.render(context)
	return view_constructor(templated_content, "Clients")

def details(request):
	content = """
		<div class='content inner-padding'>
			<h6>turnaround</h6>
			<p>Turnaround, like many other things, is negotiable. But here are some guidelines to help you plan:</p>
			<p><span class='maroon-text'>dissertation or thesis formatting:</span> Formatting can usually be done within one week, particularly if the document is otherwise complete.</p>
			<p><span class='maroon-text'>dissertation or thesis editing:</span> Turnaround for editing varies, depending on length and complexity of the material. It's best to allow three weeks or more. I don't do "rush" thesis/dissertation editing, unless only a quick proofread is needed, because rush turnaround doesn't leave time for queries or multiple rounds of revisions.</p>
			<p><span class='maroon-text'>editing other than thesis/dissertation projects:</span> For documents of 100 pages or less, turnaround is approximately one week.</p>
			<p><span class='maroon-text'>short projects:</span> Documents of 10 pages or less can usually be completed within a day or two.</p>
			<h6>payment</h6>
			<p><span class='maroon-text'>dissertation or thesis formatting or editing:</span> I require a 50% deposit before beginning a dissertation or thesis project. The final payment is due when the document is accepted by your graduate school advisor or, if filing is not imminent, when the current round of formatting/editing is complete.</p>
			<p><span class='maroon-text'>editing other than thesis/dissertation projects:</span> Full payment is due when the current round of editing revisions is complete. For larger projects, I require a deposit of 50% before beginning work; the balance is due on completion.</p>
			<p><span class='maroon-text'>repeat customers on a 30-day invoice cycle:</span> Full payment is due 30 days from invoice date.</p>
			<hr>
			<p class='center'>I accept payment by check or credit card, by wire transfer, or by company or university purchase order. If you need to make a special arrangement, ask!</p>
		</div>
	"""
	return view_constructor(content, "Details")

def faq(request):
	content = """
		<div class='content inner-padding'>
			<h6>answers to frequently asked questions</h6>
			<br/>
			<p><strong class='maroon-text'>software packages and platforms</strong>
				<br/>Word 2003, 2007, 2010 for Windows; Word 2004, 2008, and 2011 for Mac; EndNote X4, Acrobat X Pro.</p>
			<br/><p><strong class='maroon-text'>style manuals</strong>
				<br/>APA 5
				<br/>APA 6
				<br/>ASA 3
				<br/>Chicago Manual of Style (15 and 16)</p>
			<p><span class='maroon-text'>as well as variants of APA for</span>
				<br/>Argosy University
				<br/>Nova Southeastern University</p>
			<p><span class='maroon-text'>and dissertation formatting requirements for</span>
				<br/>Cornell University
				<br/>Harvard University
				<br/>Colorado State University
				<br/>University of Michigan
				<br/>University of Pennsylvania</p>
		</div>
	"""
	return view_constructor(content, "FAQ")

def securelogin(request):
	content = "<h1>secure login view</h1>"
	return view_constructor(content, "Secure Login")

def paypal(request):
	content = "<h1>paypal view</h1>"
	return view_constructor(content, "PayPal")

def contactindex(request):
	content = "<h1>contact index view</h1>"
	return view_constructor(content, "Contact")