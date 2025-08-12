import { useSelector } from "react-redux";
import "./content.css";
import NotLogin from "./sub_content/NotLogin";
import RegEatLog from "./sub_content/RegEatLog";
import TodayEat from "./sub_content/TodayEat";

const EatLogHome = () => {

    const subscriber = useSelector((store) => store.AccountSlice);

    if(!subscriber.login) return <NotLogin />
    else{
        return (
            <table id="table_EatLogHome" align="center">
                <tr>
                    <td>
                        <RegEatLog />
                    </td>
                    <td rowSpan={2} width={800}>
                    </td>
                </tr>
                <tr>
                    <td>
                        <TodayEat />
                    </td>
                </tr>
            </table>
        );
    }
};

export default EatLogHome;
