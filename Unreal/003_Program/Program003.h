// Pawn
// Program 003

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program003.generated.h"

UCLASS()
class AProgram003 : public AActor
{
    GENERATED_BODY()

public:
    AProgram003();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
