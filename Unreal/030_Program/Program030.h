// Timer Manager
// Program 030

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Program030.generated.h"

UCLASS()
class AProgram030 : public AActor
{
    GENERATED_BODY()

public:
    AProgram030();

protected:
    virtual void BeginPlay() override;

public:
    virtual void Tick(float DeltaTime) override;
};
