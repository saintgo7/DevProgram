// Apply Damage
// Program 044

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program044.generated.h"

UCLASS()
class AProgram044 : public AActor
{
    GENERATED_BODY()

public:
    AProgram044();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
