// Save Game
// Program 055

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program055.generated.h"

UCLASS()
class AProgram055 : public AActor
{
    GENERATED_BODY()

public:
    AProgram055();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
