from mpf.core.custom_code import CustomCode


class PT2Replacement(CustomCode):

    def on_load(self):
        self.machine.events.add_handler(
            "pt2_request_replacement_ball",
            self._request_replacement_ball
        )

    def _request_replacement_ball(self, **kwargs):
        del kwargs

        self.machine.playfield.add_ball(
            player_controlled=True
        )
