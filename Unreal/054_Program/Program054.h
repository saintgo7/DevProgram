// Game Instance
// Program 054

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program054.generated.h"

UCLASS()
class AProgram054 : public AActor
{
    GENERATED_BODY()

public:
    AProgram054();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
