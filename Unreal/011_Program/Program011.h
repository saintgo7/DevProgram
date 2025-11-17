// Collision Component
// Program 011

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program011.generated.h"

UCLASS()
class AProgram011 : public AActor
{
    GENERATED_BODY()

public:
    AProgram011();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
