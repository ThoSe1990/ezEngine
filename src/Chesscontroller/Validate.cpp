
#include "Chesscontroller/Validate.hpp"
#include "Chesscontroller/PlayersTurn.hpp"

#include "Movements/MovementsFactory.hpp"

Validate::Validate (const std::string& PlayerColor, const std::string& OpponentColor) : State(PlayerColor, OpponentColor)
{

}

void Validate::UpdateGame(std::shared_ptr<Chesscontroller> chesscontroller)
{
    std::shared_ptr<Entity> piece = chesscontroller->GetSelectedPiece();
    auto movements = MovementFactory::Create(chesscontroller, piece);
    movements->CreateValidMovements();

    auto next = std::make_unique<PlayersTurn>(playerColor, opponentColor);
    chesscontroller->SetState(std::move(next));
}

