// Capsule Collision
// Program 014

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program014.generated.h"

UCLASS()
class AProgram014 : public AActor
{
    GENERATED_BODY()

public:
    AProgram014();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
