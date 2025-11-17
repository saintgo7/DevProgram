// Add Impulse
// Program 064

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program064.generated.h"

UCLASS()
class AProgram064 : public AActor
{
    GENERATED_BODY()

public:
    AProgram064();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
