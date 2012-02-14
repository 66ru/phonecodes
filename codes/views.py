from utils import response_json
from utils.exceptions import OperatorNotFoundException, NotPostRequestException, WrongNumberException
from models import Operator
from forms import PhoneForm

def show_operator(request):
    try:
        if request.method != 'POST':
            raise NotPostRequestException

        else:
            form = PhoneForm(request.POST)
            if form.is_valid():
                phone = form.cleaned_data['phone']
                operator = Operator.find(phone)

                if operator:
                    response = {'status': 0, 'message': 'ok', 'operator': operator.name, 'region': operator.region}
                else:
                    raise OperatorNotFoundException

            else:
                raise WrongNumberException

    except (OperatorNotFoundException, NotPostRequestException, WrongNumberException), e:
        return response_json({'status': 1, 'message': e.msg})

    except Exception, e:
        return response_json({'status': 1, 'message': e})

    return response_json(response)