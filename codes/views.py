from utils import response_json
from utils.exceptions import OperatorNotFoundException, InvalidNumberException
from models import Operator
from forms import PhoneForm

def show_operator(request):
    try:
        if request.method != 'POST':
            form = PhoneForm(request.GET)
        else:
            form = PhoneForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            operator = Operator.find(phone)

            if operator:
                response = {
                    'status': 0,
                    'message': 'ok',
                    'phone': phone,
                    'operator': operator.name,
                    'region': operator.region,
                    'mobile': operator.mobile,
                }
            else:
                raise OperatorNotFoundException

        else:
            raise InvalidNumberException

    except (OperatorNotFoundException, InvalidNumberException), e:
        return response_json({'status': 1, 'message': e.msg})

    except Exception, e:
        return response_json({'status': 1, 'message': e})

    return response_json(response)