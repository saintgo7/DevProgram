// Simulate Physics
// Program 062

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program062.generated.h"

UCLASS()
class AProgram062 : public AActor
{
    GENERATED_BODY()

public:
    AProgram062();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
